from langchain_text_splitters import RecursiveCharacterTextSplitter
import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import json
import streamlit as st


def generate_embeddings():
    # import dataset
    df = pd.read_csv('./Datasets/Standards - Catalogue Data - 28 Jan 2026.csv', encoding='utf-8')

    # to filter, only choose standards documents
    df = df[df['category'] == 'Standard']


    df = df.fillna("")
    df["document_text"] = df.apply(row_to_text, axis=1)
    df["document_text"] = df["document_text"].astype(str)
    df_clean = df['document_text']


    chunks = create_chunks(df, df_clean)

    model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

    texts = [chunk['content'] for chunk in chunks]
    # embeddings = model.encode(texts, convert_to_numpy=True, show_progress_bar=True)


    # faiss_index = create_faiss_index(embeddings, embedding_dim=embeddings.shape[1])
    # save_index(faiss_index)

    batch_size = 32
    all_embeddings = []
    progress_bar = st.progress(0, text="Generating embeddings...")

    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        batch_embeddings = model.encode(batch, convert_to_numpy=True)
        all_embeddings.append(batch_embeddings)

        pct = min(int(((i + batch_size) / len(texts)) * 100), 100)
        progress_bar.progress(pct, text=f"Embedding {min(i + batch_size, len(texts))}/{len(texts)} chunks...")

    embeddings = np.vstack(all_embeddings)
    progress_bar.progress(100, text="✅ Embeddings complete!")

    faiss_index = create_faiss_index(embeddings, embedding_dim=embeddings.shape[1])
    save_index(faiss_index)

    


def row_to_text(row):
    parts = []

    if row["title"]:
        parts.append(f"Title: {row['title']}")
    if row["subtitle"]:
        parts.append(f"Subtitle: {row['subtitle']}")
    if row["description"]:
        parts.append(f"Description: {row['description']}")
    if row["body"]:
        parts.append(f"Body: {row['body']}")
    if row["keywords"]:
        parts.append(f"Keywords: {row['keywords']}")

    return "\n".join(parts)

# def create_faiss_index(embeddings, embedding_dim, nlist=40):
#     embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
#     quantizer = faiss.IndexFlatL2(embedding_dim)
#     index = faiss.IndexIVFFlat(quantizer, embedding_dim, nlist, faiss.METRIC_INNER_PRODUCT)
    
#     index.train(embeddings)
#     index.add(embeddings)
#     index.nprobe = 10
#     return index

def create_faiss_index(embeddings, embedding_dim):
    embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
    index = faiss.IndexFlatL2(embedding_dim)
    index.add(embeddings)
    return index


def save_index(index, index_path='faiss_index.bin'):
    faiss.write_index(index, index_path)
    print (index_path + " created")



def create_chunks(df, df_clean):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,     
        chunk_overlap=80,
        separators=["\n\n","\n",". "," ",""]
    )

    chunks = []
    for i, doc in enumerate(df_clean):
        split_chunk = splitter.split_text(doc)

        for id, chunk in enumerate(split_chunk):
            chunks.append({
                "doc_id": i,
                "chunk_id": id,
                "content" : chunk,
                "title": df.iloc[i]['title']
            })


    with open("chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    return chunks


if __name__ == "__main__":
   generate()