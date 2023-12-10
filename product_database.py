from sentence_transformers import SentenceTransformer
from transformers import AutoModel
import faiss
import numpy as np
import pickle

# local config module
import config

"""
Creates product database based on config
"""
def make_product_database():

    # Model used for embeddings
    model = AutoModel.from_pretrained(config.transformer_model, trust_remote_code=True) # trust_remote_code is needed to use the encode method

    # Creates FAISS index, dimensions can be configured based on model used for embeddings
    index = faiss.IndexFlatL2(config.dimensions)

    # Pulls key:value for embeddings, may be updated/adjusted in config file
    product_categories  = config.product_categories

    # Mapping for embeddings in the index to original key:value pairs from categories
    product_embeddings_mapping = {}
    current_index = 0

    # Creates embeddings
    for product, descriptions in product_categories.items():
        for description in descriptions:
            embedding = model.encode(description)
            index.add(np.array([embedding]))
            product_embeddings_mapping[current_index] = product
            current_index += 1

    # Saves FAISS index of embeddings to directory 
    faiss.write_index(index, "embeddings/product_embeddings.index")
    with open('embeddings/product_mapping.pk1', 'wb') as f:
        pickle.dump(product_embeddings_mapping, f)