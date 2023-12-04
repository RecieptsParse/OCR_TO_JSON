### Imports ###
from pydantic import BaseModel, Field, field_validator
from typing import List
from enum import Enum
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.chat_models import ChatOpenAI
import os
import openai

# local prompt_examples module
from prompt_examples import get_prompt_examples

# '''
# Defining a subitem to be used for the includedItems category in the Item object.
# The includedItems fields consists of a list of SubItems and can be empty.
# For example, a 'cheesburger' Item might have includedItems:['bun', 'patty', 'cheese']
# '''
# class SubItem(BaseModel):
#     description: str

'''
An enumeration of the types of payment methods for the paymentType category in the ReceiptInfo object.
The default in ReceiptInfo is 'cash'.
'''   
class PaymentType(Enum):
    CREDIT = 'credit'
    DEBIT = 'debit'
    CASH = 'cash'

'''
This object represents a single item (good/service) that was purchased in the receipt text.
'''
class Item(BaseModel):
    description: str=Field(description="item name")
    unabbreviatedDescription: str=Field(default="", description="unabbreviated name of field:description")
    includedItems: List[str]=Field(default_factory=list)
    quantity: int=Field(description="number of items")
    unitPrice: float=Field(description="cost per unit")
    totalPrice: float=Field(description="total cost of unit(s) purchased")
    discountAmount: float=Field(description="discount for item")
    
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
    paymentType: PaymentType=Field(default="cash", description="payment method")
    creditCardType: str=Field(default="<UNKNOWN>", description="credit card type")
    totalDiscount: float=Field(default=0.00, description="total discount")
    tax: float=Field(description="tax amount")
    total: float=Field(description="total amount paid")
    ITEMS: List[Item]
    
    @field_validator('paymentType', mode="before")
    def validate_paymentType(cls, paymentType: str) -> PaymentType:
        string = paymentType.lower()
        returnValue = PaymentType.CASH
        if 'credit' in string:
            returnValue = PaymentType.CREDIT
        elif 'debit' in string:
            returnValue = PaymentType.DEBIT
        return returnValue

# <-- Break Point --> 
def make_receiptParser():
    return PydanticOutputParser(pydantic_object=ReceiptInfo)

def get_prompt_prefix():
    return '''You are a capable large language model. Your task is to extract data from a given receipt and format it into the JSON schema below. Use the default values if you're not sure. Try to infer a value for the field: unabbreviatedDescription. The values for the fields: description and unnabbreviatedDescription can not be the same. Text can be used for multiple fields. Please use double-quotes for all string values.
    
    {format_instructions}
    
    '''

def get_example_prompt(input_variables=["ExampleInput", "ExampleOutput"], template= "input:\n{ExampleInput}\noutput:\n{ExampleOutput}"):
    return (PromptTemplate(input_variables = input_variables, template = template))

def get_suffix():
    return "input:\n{input}\noutput:\n"

def make_fewshot_prompt(receiptParser):
    return (FewShotPromptTemplate(
    prefix = get_prompt_prefix(),
    input_variables=["input"], 
    partial_variables={'format_instructions': receiptParser().get_format_instructions()},
    examples=get_prompt_examples(),
    example_prompt = get_example_prompt(),
    example_separator="\n",
    suffix = get_suffix(),
    ))

def make_model(model="gpt-3.5-turbo-16k", temperature=1.00, openai_api_key="INSERT_OPENAI_API KEY"):
    return ChatOpenAIChatOpenAI(model=model, temperature=temperature, openai_api_key=openai_api_key)

def make_chain(fewshot_prompt, model, receiptParser):
    chain = execute_fewshot_prompt | model | receiptParser
    return chain