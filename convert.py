### Imports ###
from pydantic import BaseModel, Field, field_validator
from typing import List
from enum import Enum
import math
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.chat_models import ChatOpenAI
import os
import openai
import typing

# local prompt_examples module
from prompt_examples import get_prompt_examples

'''
This object represents a single item (good/service) that was purchased in the receipt text.
'''
class Item(BaseModel):
    description: str=Field(description="item name")
    unabbreviatedDescription: str=Field(default="", description="unabbreviated name of field:description")
    includedItems: List[str]=Field(default_factory=list)
    quantity: int=Field(default=0, description="number of items")
    unitPrice: float=Field(default=0.00, description="cost per unit")
    totalPrice: float=Field(default=0.00, description="total cost of unit(s) purchased")
    discountAmount: float=Field(default=0.00, description="discount for item")

    @field_validator('unitPrice', 'totalPrice', 'discountAmount', mode='before')
    @classmethod
    def validate_float_Item(cls, input_value: typing.Any) -> float:
        return_value = 0.00
        if (isinstance(input_value, str)):
            try:
                return_value = (float(input_value))
            except:
                return_value = 0.00
        elif (isinstance(input_value, int)):
            return_value = float(input_value)
        elif (isinstance(input_value, float)):
            return_value = input_value
        return return_value
    
    @field_validator('quantity', mode='before')
    @classmethod
    def validate_quantity(cls, quantity: typing.Any) -> int:
        return_value = 0
        if (isinstance(quantity, str)):
            try:
                return_value = math.ceil(float(quantity))
            except:
                return_value = 0
        elif (isinstance(quantity, int)):
            return_value = quantity
        elif (isinstance(quantity, float)):
            return_value = math.ceil(quantity)
        return return_value
    
    @field_validator('description', 'unabbreviatedDescription', mode='after')
    @classmethod
    def validate_string_Item(cls, input_value: str) -> str:
        return_value = input_value.replace("<UNKNOWN>", "")
        return_value = return_value.replace("UNKNOWN", "")
        return_value = " ".join(return_value.split())
        return return_value
    
    @field_validator('includedItems', mode='after')
    @classmethod
    def validate_includedItems(cls, includedItems):
        return_array = []
        for item in includedItems:
            new_item = item.replace("<UNKNOWN>", "")
            new_item = new_item.replace("UNKNOWN", "")
            new_item = " ".join(new_item.split())
            if new_item:
                return_array.append(new_item)
        return return_array

    
'''
This object represents the all of the information residing in one receipt text file.
Raw receipt text files are to be parsed into JSON object format for use in later analysis.
'''
class ReceiptInfo(BaseModel):
    merchant: str=Field(description="name of merchant")
    address: str=Field(description="address")
    city: str=Field(description="city")
    state: str=Field(description="state")
    phoneNumber: str=Field(description="phone number")
    receiptDate: str=Field(description="purchase date")
    receiptTime: str=Field(description="time purchased")
    totalItems: int=Field(description="number of items")
    diningOptions: str=Field(default="", description="here or to-go items for consumable items")
    paymentType: str=Field(default="cash", description="payment method")
    creditCardType: str=Field(default="", description="credit card type")
    totalDiscount: float=Field(default=0.00, description="total discount")
    tax: float=Field(description="tax amount")
    total: float=Field(description="total amount paid")
    ITEMS: List[Item]
    
    @field_validator('totalItems', mode='before')
    @classmethod
    def validate_totalItems(cls, totalItems: typing.Any) -> int:
        return_value = 0
        if (isinstance(totalItems, str)):
            try:
                return_value = math.ceil(float(totalItems))
            except:
                return_value = 0
        elif (isinstance(totalItems, int)):
            return_value = totalItems
        elif (isinstance(totalItems, float)):
            return_value = math.ceil(totalItems)
        return return_value

    @field_validator('paymentType', mode='before')
    def validate_paymentType(cls, paymentType: str) -> str:
        return_value = 'cash'
        try:
            string = paymentType.lower()
            credit_card_names = ['visa', 'discover', 'mastercard', 'american', 'express', 'amex', 'chase', 'citi', 'credit', 'card']
            if 'debit' in string:
                return_value = 'debit'
            else:
                for term in credit_card_names:
                    if term in string:
                        return_value = 'credit'
        except:
            pass
        return return_value
    
    @field_validator('diningOptions', mode='before')
    @classmethod
    def validate_diningOptions(cls, diningOptions: str) -> str:
        return_value = ''
        try:
            string = diningOptions.lower()
            dine_in_terms = ['for', 'here', 'dine', 'in', 'house', 'on']
            to_go_terms = ['take', 'out', 'carry', 'to', 'go', 'pick', 'up', 'delivery', 'grab', 'away']
            dine_in_score = sum([string.__contains__(term) for term in dine_in_terms])
            to_go_score = sum([string.__contains__(term) for term in to_go_terms])
            if (dine_in_score > to_go_score):
                return_value = 'DINE IN'
            elif (dine_in_score < to_go_score):
                return_value = 'TO GO'
            elif ((dine_in_score != 0) and (to_go_score != 0) and (dine_in_score == to_go_score)):
                return_value = 'TO GO'
        except:
            pass
        return return_value

    @field_validator('tax', 'total', 'totalDiscount', mode='before')
    @classmethod
    def validate_float_ReceiptInfo(cls, input_value: typing.Any) -> float:
        return_value = 0.00
        if (isinstance(input_value, str)):
            try:
                return_value = float(input_value)
            except:
                return_value = 0.00
        elif (isinstance(input_value, int)):
            return_value = float(input_value)
        elif (isinstance(input_value, float)):
            return_value = input_value
        else:
            return_value = 0.00
        return return_value
    
    @field_validator('merchant', 'address', 'city', 'state', 'phoneNumber', 
                     'receiptDate', 'receiptTime', 'creditCardType', mode='after')
    @classmethod
    def validate_string_ReceiptInfo(cls, input_value: str) -> str:
        return_value = input_value.replace("<UNKNOWN>", "")
        return_value = return_value.replace("UNKNOWN", "")
        return_value = " ".join(return_value.split())
        return return_value
             
def make_receiptParser():
    return PydanticOutputParser(pydantic_object=ReceiptInfo)

def get_prompt_prefix():
    return '''You are a capable large language model. 
    Your task is to extract data from a given receipt and format it into the JSON schema below. 
    Use the default values if you're not sure. From the item description please predict the unabbreviatedDescription. 
    The values for the fields "description" and "unnabbreviatedDescription" can not be the same. 
    Please wrap all numeric values in double-quotes. Some items may be priced at a weighted rate, such as "per pound" or "per ounce". 
    Text can be used for multiple fields. Please use double-quotes for all string values. 
    If there are double-quotes inside string values, please escape those characters with the "\" character.
    
    {format_instructions}
    
    '''

def get_example_prompt(input_variables=["ExampleInput", "ExampleOutput"], template= "input:\n{ExampleInput}\noutput:\n{ExampleOutput}"):
    return (PromptTemplate(input_variables = input_variables, template = template))

def get_suffix():
    return "input:\n{input}\noutput:\n"

def make_fewshot_prompt(format_instructions):
    return (FewShotPromptTemplate(
    prefix = get_prompt_prefix(),
    input_variables=["input"], 
    partial_variables={'format_instructions': format_instructions},
    examples=get_prompt_examples(),
    example_prompt = get_example_prompt(),
    example_separator="\n",
    suffix = get_suffix(),
    ))

def make_model(model="gpt-3.5-turbo-16k", temperature=1.00, openai_api_key="INSERT_OPENAI_API KEY"):
    return ChatOpenAI(model=model, temperature=temperature, openai_api_key=openai_api_key)

def make_chain(fewshot_prompt, model, receiptParser):
    chain = fewshot_prompt | model | receiptParser
    return chain
