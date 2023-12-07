from collections import Counter
from sentence_transformers import SentenceTransformer
from transformers import AutoModel
import numpy as np
import faiss
import pickle

# local config module
import config

# Shared model initialization
#model = SentenceTransformer(config.transformer_model)
model = AutoModel.from_pretrained('jinaai/jina-embeddings-v2-base-en', trust_remote_code=True) # trust_remote_code is needed to use the encode method


class Classifier:
    def __init__(self, index_path, mapping_path):
        self.model = model
        self.index = None
        self.mapping = None
        self.index_path = index_path
        self.mapping_path = mapping_path

    def load_resources(self):
        if self.index is None:
            self.index = faiss.read_index(self.index_path)
        if self.mapping is None:
            with open(self.mapping_path, 'rb') as f:
                self.mapping = pickle.load(f)

    def search(self, query, k):
        self.load_resources()
        embedding = self.model.encode(query)
        _, indices = self.index.search(np.array([embedding]), k)
        results = [self.mapping[idx] for idx in indices[0]]
        most_common_result = Counter(results).most_common(1)[0][0]
        return most_common_result

# Function to get the classifier
def get_classifier(classifier_type):
    if classifier_type == "vendor":
        return Classifier("vendor_embeddings.index", "vendor_mapping.pk1")
    elif classifier_type == "product":
        return Classifier("product_embeddings.index", "product_mapping.pk1")
    else:
        raise ValueError("Invalid classifier type")

def query_classification(query, k, classifier_type):
    classifier = get_classifier(classifier_type)
    return classifier.search(query, k)
