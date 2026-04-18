import faiss
from sentence_transformers import SentenceTransformer
import numpy as np
import json
from user_input import generate
import streamlit as st




def generate_topk(k=10):
    
    index = faiss.read_index("faiss_index.bin")

    # file_path = 'output.txt'

    with open("chunks.json", "r", encoding="utf-8") as f:
        chunks = json.load(f)

    # with open(file_path, 'r') as file:
    #     user_input = file.read()

    user_input = generate()

    model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

    query_embedding = model.encode(user_input)
    query_embedding = query_embedding / np.linalg.norm(query_embedding, axis=1, keepdims=True)

    D, I = index.search(query_embedding, k=k)

    print_topk(D, I, chunks)

def print_topk(D, I, chunks):
    print("\nTop K Results:\n")

    for rank, idx in enumerate(I[0]):
        chunk = chunks[idx]
        score = D[0][rank]

        st.write(f"Rank {rank+1}")
        st.write(f"Score: {score:.4f}")
        st.write(f"Doc ID: {chunk['doc_id']} | Chunk ID: {chunk['chunk_id']}")
        st.write(f"Title: {chunk['title']}")
        st.write(f"Content: {chunk['content']}")
        st.write("-" * 60)


