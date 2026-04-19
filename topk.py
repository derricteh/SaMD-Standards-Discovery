import faiss
from sentence_transformers import SentenceTransformer
import numpy as np
import json
from user_input import generate
import streamlit as st




def generate_topk(k=10):
    
    index = faiss.read_index("faiss_index.bin")

    with open("chunks.json", "r", encoding="utf-8") as f:
        chunks = json.load(f)

    subqueries = generate()

    model = SentenceTransformer('BAAI/bge-large-en-v1.5')

    all_results = {}  

    for query in subqueries:
        query_with_prefix = "Represent this sentence for searching relevant passages: " + query
        query_embedding = model.encode(query_with_prefix, convert_to_numpy=True)
        query_embedding = query_embedding / np.linalg.norm(query_embedding)
        query_embedding = query_embedding.reshape(1, -1)

        D, I = index.search(query_embedding, k=k)

        for score, idx in zip(D[0], I[0]):
            if idx not in all_results or score > all_results[idx]['score']:
                all_results[idx] = {
                    'score': score,
                    'chunk': chunks[idx]
                }

    sorted_results = sorted(all_results.values(), key=lambda x: x['score'], reverse=True)[:k]

    print_topk(sorted_results)


def print_topk(results):
    st.write("\nTop K Results:\n")

    for rank, result in enumerate(results):
        chunk = result['chunk']
        score = result['score']

        with st.expander(f"Rank {rank + 1} — {chunk['title']} (Score: {score:.4f})"):
            st.markdown(f"**Doc ID:** {chunk['doc_id']} | **Chunk ID:** {chunk['chunk_id']}")
            st.markdown(f"**Score:** {score:.4f}")
            st.markdown(f"**Content:**")
            st.write(chunk['content'])

