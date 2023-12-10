import vendor_database
import product_database
import convert
import os
import json
import pandas as pd
import sys
import subprocess

openai_api_key="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"

# Check if the required number of arguments is provided
if len(sys.argv) < 3:
    print("Insufficient arguments. Please provide both input and output paths.")
    sys.exit(1)

input_path = sys.argv[1]  # The path to the folder containing .txt files
output_path = sys.argv[2]  # The path to the output file

try:
    subprocess.run(['/bin/bash', 'install_packages.sh'], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running shell script: {e}")

print(f"Processing receipts from {input_path} and saving to {output_path}")

'''
saves faiss index and mapping to directory 
model for embeddings & descriptions can be updated in config.py
'''
vendor_database.make_vendor_database()
product_database.make_product_database()

'''
Convert raw receipt text to JSON objects and store the JSON objects as strings in 
'''

#receipts_folder = "data/receipts/text" # the folder that contains raw receipt text files to convert to JSON
receipts_folder = input_path

# Set up the main components of the JSON conversion process
receiptParser = convert.make_receiptParser()
fewshot_prompt = convert.make_fewshot_prompt(receiptParser.get_format_instructions())
model = convert.make_model(model="gpt-4-1106-preview", temperature=1.00, openai_api_key=openai_api_key)
chain = convert.make_chain(fewshot_prompt, model, receiptParser)

# Calculate total number of .txt files
total_files = len([name for name in os.listdir(receipts_folder) if name.endswith('.txt')])

# Iterate through receipts_folder, and convert each receipt to a JSON object
for i, filename in enumerate(os.listdir(receipts_folder)):
    if filename.endswith('.txt'):
        with open(os.path.join(receipts_folder, filename)) as f:
            data = f.read()
            response = chain.invoke({"input": data})
            # with 'a' in open() it will create or append to current file
            with open(output_path, 'a') as fp: # Write each JSON object as it gets parsed
                    # write each receipt JSON on a new line
                    fp.write(json.dumps({"ReceiptInfo": json.loads(response.model_dump_json())}) + "\n") 

        # Calculate and print the progress
        percent_complete = ((i + 1) / total_files) * 100
        sys.stdout.write(f"\rProgress: {percent_complete:.2f}% completed")
        sys.stdout.flush()

print(f", master.py completed, JSON file saved to {output_path}")