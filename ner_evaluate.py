import os
import json
from nervaluate import Evaluator

def find_span(text, entity_text):
    start = text.find(entity_text)
    if start == -1:
        return (-1, -1), entity_text
    end = start + len(entity_text)
    return (start, end), entity_text

def convert_to_prodigy_spans(receipt_text, entities):
    text_vals = {}
    #entities = json.loads(entities)
    prodigy_data = []
    receipt_info = entities["ReceiptInfo"]

    for label, entity_text in [
        ("MERCHANT", receipt_info["merchant"]),
        ("ADDRESS", receipt_info["address"]),
        ("CITY", receipt_info["city"]),
        ("STATE", receipt_info["state"]),
        ("PHONE", receipt_info["phoneNumber"]),
        ("TAX", str(receipt_info["tax"])),
        ("TOTAL", str(receipt_info["total"])),
        ("DATE", receipt_info["receiptDate"]),
        ("TIME", receipt_info["receiptTime"])
    ]:
        span, text = find_span(receipt_text, entity_text)
        text_vals[label] = text
        if span:
            start, end = span
            prodigy_data.append({"start": start, "end": end, "label": label})

    # Process item-level entities
    for item in receipt_info["ITEMS"]:
        discount = ""
        if(item["discountAmount"] != 0.00):
            discount = str(item["discountAmount"])
        for label, entity_text in [
            ("ITEM_DESC", item["description"]),
            ("QTY", str(item["quantity"])),
            ("UNIT_PRICE", str(item["unitPrice"])),
            ("TOTAL_PRICE", str(item["totalPrice"])),
            ("DISCOUNT", discount)  # Discount might not always be present in the raw receipt text
        ]:
            if entity_text:  # Check if the entity text is not empty
                span, text = find_span(receipt_text, entity_text)
                text_vals[label] = text
                if span:
                    start, end = span
                    prodigy_data.append({"start": start, "end": end, "label": label})
    return prodigy_data, text_vals


ner_eval_folder = "data/receipts/ner_evaluate" # used to grab the raw receipt texts
golden_annotations_path = "data/receipts/ner_evaluate/annotations/golden_annotations.json" # used to grab the "true" annotations
classified_annotations_path = "data/receipts/ner_evaluate/annotations/classified_ner_evaluate.json" # used to the grab the generated annotations

# Create empty list objects to hold multiple JSON objects and/or receipt texts
golden_annotations=[]
classified_annotations = []
receipt_texts = []
ner_scores_golden = []
ner_scores_classified = []
overall_results = []
overall_results_per_tag = []

# Because the generated annotations are in an array format, read them all at once
with open(classified_annotations_path, 'r') as f:
    classified_annotations = json.load(f)
    
# Because the "true" annotations are separated by line (i.e. a each JSON object has a separate line), read them line-by-line
with open(golden_annotations_path, 'r') as f:
    lines = f.readlines()
    for line in lines:
         json_object = json.loads(line)
         golden_annotations.append(json_object)

# Read in the raw receipt text, while also replacing any UNKNOWN values from OCR and any whitespace to make NER-Evaluate more accurate
for filename in os.listdir(ner_eval_folder):
    if filename.endswith('.txt'):
        with open(os.path.join(ner_eval_folder, filename)) as f:
            return_value = f.read().replace("<UNKNOWN>", "")
            return_value = return_value.replace("UNKNOWN", "")
            return_value = return_value.replace("Unknown", "")
            return_value = return_value.replace("unknown", "")
            return_value = " ".join(return_value.split())
            receipt_texts.append(return_value)

# For each "true" annotation, find the value of each identifiable field from the raw receipt text and note its start/stop position
for pair in zip(receipt_texts, golden_annotations):
    prodigy_spans, text_vals = convert_to_prodigy_spans(pair[0], pair[1])
    ner_scores_golden.append({"scores": prodigy_spans, "text_values": text_vals})
    
# For each generated annotation, find the value of each identifiable field from the raw receipt text and note its start/stop position
for pair in zip(receipt_texts, classified_annotations):
    prodigy_spans, text_vals = convert_to_prodigy_spans(pair[0], pair[1])
    ner_scores_classified.append({"scores": prodigy_spans, "text_values": text_vals})

# Lastly, compare the "true" annotation scores and the generated annotation scores against each other.
# Store the results PER RECEIPT in overall_results and overall_results_per_tag
for pair in zip(ner_scores_golden, ner_scores_classified):
    true = [[score] for score in pair[0]['scores']]
    pred = [[score] for score in pair[1]['scores']]
    results, results_per_tag = Evaluator(true, pred, 
                                         tags=['MERCHANT', 'ADDRESS', 'CITY', 'STATE', 'PHONE', 'TAX', 'TOTAL', 'DATE', 'TIME', 'ITEM_DESC', 'QTY', 'UNIT_PRICE', 'TOTAL_PRICE']
                                        ).evaluate()
    overall_results.append(results)
    overall_results_per_tag.append(results_per_tag)
