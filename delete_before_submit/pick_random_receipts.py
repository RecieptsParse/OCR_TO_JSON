import os
import shutil
import random

'''
This file chooses (num_files) numbers of files from data/receipts/text for NER-Evaluation.
For context, data/receipts/text is the folder that contains all the raw receipt text files.

------------------------------------------WARNING------------------------------------------
Once run, this program will completely change the receipts used for NER-Evaluation, which
means that the hand-annotated NER-Evaluate golden annotations will no longer be valid! 
Please keep this in mind before running this program.
'''

# How many files to pick randomly for NER-Evaluation
num_files = 10

# Parent folder for both the raw text and NER-evaluate folders
receipts_folder = "data/receipts"

# (raw receipt text folder) path name and files
raw_text_folder = f"{receipts_folder}/text"
raw_text_files = os.listdir(raw_text_folder)

# NER-Evaluate path name and files
ner_evaluate_folder = f"{receipts_folder}/ner_evaluate"
ner_evaluate_files = os.listdir(ner_evaluate_folder)

# Clear out the existing files in data/receipts/ner_evaluate
for file in ner_evaluate_files:
    if file.endswith('.txt'):
        relative_file_path = os.path.join(ner_evaluate_folder, file)
        if os.path.exists(relative_file_path):
            os.remove(relative_file_path)

# Pick 10 random files from data/receipts/text to use for NER-Evaluation
i = 0
while i < num_files:
    random_file = random.choice(raw_text_files)
    if random_file.endswith('.txt'):
        with open(os.path.join(raw_text_folder, random_file)) as f:
            copy_to_path = f"{receipts_folder}/ner_evaluate/{random_file}"
            print(copy_to_path)
            shutil.copy(f.name, copy_to_path)
            i += 1
            # since this chunk doesn't run unless a .txt file is encountered, (num_files) number of files will always be chosen