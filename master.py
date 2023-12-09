import vendor_database
import product_database
import classification
import convert
import os
import json
import pandas as pd
import csv
import sys
import subprocess


try:
    subprocess.run(['/bin/bash', 'install_packages.sh'], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running shell script: {e}")

'''
saves faiss index and mapping to directory 
model for embeddings & descriptions can be updated in config.py
'''
vendor_database.make_vendor_database()
product_database.make_product_database()

'''
Convert raw receipt text to JSON objects and store the JSON objects as strings in 
'''

receipts_folder = "data/receipts/text" # the folder that contains raw receipt text files to convert to JSON

openai_api_key="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"

# Set up the main components of the JSON conversion process
receiptParser = convert.make_receiptParser()
fewshot_prompt = convert.make_fewshot_prompt(receiptParser.get_format_instructions())
model = convert.make_model(model="gpt-4-1106-preview", temperature=1.00, openai_api_key=openai_api_key)
chain = convert.make_chain(fewshot_prompt, model, receiptParser)

# If a sys_arg was passed (for number of files to skip), note it down
skip_num_files = 0
if((len(sys.argv) - 1) > 0):
    skip_num_files = int(sys.argv[1])

# Iterate through receipts_folder, and convert each receipt to a JSON object
i=0
for filename in os.listdir(receipts_folder):
    if filename.endswith('.txt'):
        i+= 1
        if i < skip_num_files:
            continue
        if filename.endswith('.txt'):
            with open(os.path.join(receipts_folder, filename)) as f:
                data = f.read()
                print('\n')
                print(f'reading from {filename}')
                response = chain.invoke({"input": data})
                # with 'a' in open() it will create or append to current file
                with open('receipts_json.json', 'a') as fp: # Write each JSON object as it gets parsed
                        # write each receipt JSON on a new line
                        fp.write(json.dumps({"ReceiptInfo": json.loads(response.model_dump_json())}) + "\n")
        print(f'Done converting {filename}, JSON located at line {i}')    

# receipts = classification.read_json_receipts("receipts_json.json")
# classification.classify(receipts)

print("PROGRAM END")