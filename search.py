from collections import Counter
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import pickle

# local config module
import config

# Shared model initialization
model = SentenceTransformer(config.transformer_model)

class Classifier:
    def __init__(self, index_path, mapping_path):
        self.model = model
        self.index = faiss.read_index(index_path)
        with open(mapping_path, 'rb') as f:
            self.mapping = pickle.load(f)

    def search(self, query, k):
        embedding = self.model.encode(query)
        _, indices = self.index.search(np.array([embedding]), k)
        results = [self.mapping[idx] for idx in indices[0]]
        most_common_result = Counter(results).most_common(1)[0][0]
        return most_common_result

# Initialize Classifier for vendors and products
vendor_classifier = Classifier("vendor_embeddings.index", "vendor_mapping.pkl")
product_classifier = Classifier("product_embeddings.index", "product_mapping.pkl")

def query_classification(query, k, classifier):
    return classifier.search(query, k)
