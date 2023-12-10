from sentence_transformers import SentenceTransformer
from transformers import AutoModel
import faiss
import numpy as np
import pickle

# local config module
import config

"""
Creates vendor database
"""
def make_vendor_database():

    #model = SentenceTransformer(config.transformer_model)

    #embedding model, can be changed in config file, some models may need a different implementation 
    model = AutoModel.from_pretrained(config.transformer_model, trust_remote_code=True) # trust_remote_code is needed to use the encode method

    # Creates FAISS index, dimensions can be configured based on model used for embeddings
    index = faiss.IndexFlatL2(config.dimensions)

    # Pulls key:value for embeddings, may be updated/adjusted in config file
    vendor_categories  = config.vendor_categories

    # Mapping for embeddings in the index to original key:value pairs from categories
    vendor_embeddings_mapping = {}
    current_index = 0

    # Creates embeddings
    for vendor, descriptions in vendor_categories.items():
        for description in descriptions:
            embedding = model.encode(description)
            index.add(np.array([embedding]))
            vendor_embeddings_mapping[current_index] = vendor
            current_index += 1

    # Saves FAISS index of embeddings to directory 
    faiss.write_index(index, "embeddings/vendor_embeddings.index")
    with open('embeddings/vendor_mapping.pk1', 'wb') as f:
        pickle.dump(vendor_embeddings_mapping, f)