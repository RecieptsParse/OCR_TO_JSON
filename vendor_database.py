from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

# local config module
import config

def make_vendor_database():

    model = SentenceTransformer(config.transformer_model)
    index = faiss.IndexFlatL2(config.dimensions)

    vendor_categories  = config.vendor_categories

    vendor_embeddings_mapping = {}
    current_index = 0

    for vendor, descriptions in vendor_categories.items():
        for description in descriptions:
            embedding = model.encode(description)
            index.add(np.array([embedding]))
            vendor_embeddings_mapping[current_index] = vendor
            current_index += 1

    faiss.write_index(index, "vendor_embeddings.index")
    with open('vendor_mapping.pk1', 'wb') as f:
        pickle.dump(vendor_embeddings_mapping, f)