# from langchain_text_splitters import RecursiveCharacterTextSplitter
# import pandas as pd
# from sentence_transformers import SentenceTransformer
# import numpy
# import faiss


# model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

# file_path = 'output.txt'

# with open(file_path, 'r') as file:
#     content = file.read()


# def create_faiss_index(embeddings, embedding_dim, nlist=10):
#     if len(embeddings) < 100:
#         index = faiss.IndexFlatIP(embedding_dim)
#         index.add(embeddings)
#     else:
#         quantizer = faiss.IndexFlatIP(embedding_dim)
#         nlist = int(len(embeddings) ** 0.5)
#         index = faiss.IndexIVFFlat(quantizer, embedding_dim, nlist, faiss.METRIC_L2)
#         index.train(embeddings)
#         index.add(embeddings)
#     return index

# def save_index(index, index_path='faiss_index_input.bin'):
#     faiss.write_index(index, index_path)

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=100,     
#     chunk_overlap=0,
# )

# chunks = splitter.split_text(content)
    
# embeddings = model.encode(chunks, convert_to_numpy=True, show_progress_bar=True)

# faiss_index = create_faiss_index(embeddings, embedding_dim=embeddings.shape[1], nlist=int(len(embeddings) ** 0.5))

# save_index(faiss_index)
