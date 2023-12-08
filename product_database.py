from sentence_transformers import SentenceTransformer
from transformers import AutoModel
import faiss
import numpy as np
import pickle

# local config module
import config

def make_product_database():
    model = AutoModel.from_pretrained(config.transformer_model, trust_remote_code=True) # trust_remote_code is needed to use the encode method


    index = faiss.IndexFlatL2(config.dimensions)

    product_categories  = config.product_categories

    product_embeddings_mapping = {}
    current_index = 0

    for product, descriptions in product_categories.items():
        for description in descriptions:
            embedding = model.encode(description)
            index.add(np.array([embedding]))
            product_embeddings_mapping[current_index] = product
            current_index += 1

    faiss.write_index(index, "embeddings/product_embeddings.index")
    with open('embeddings/product_mapping.pk1', 'wb') as f:
        pickle.dump(product_embeddings_mapping, f)