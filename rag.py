import os

import streamlit as st

from dotenv import load_dotenv

from huggingface_hub import InferenceClient

from langchain_community.vectorstores import FAISS

from langchain_community.embeddings import HuggingFaceEmbeddings

# ----------------------------------------------------
# Load Environment Variables
# ----------------------------------------------------

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
print("HF_TOKEN:", HF_TOKEN)

MODEL_NAME = "meta-llama/Llama-3.1-8B-Instruct"

# ----------------------------------------------------
# Hugging Face Client
# ----------------------------------------------------

client = InferenceClient(
    model=MODEL_NAME,
    token=HF_TOKEN
)

# ----------------------------------------------------
# Load Embedding Model
# ----------------------------------------------------

@st.cache_resource
def load_embedding():

    embedding = HuggingFaceEmbeddings(

        model_name="sentence-transformers/all-MiniLM-L6-v2"

    )

    return embedding

# ----------------------------------------------------
# Load FAISS Index
# ----------------------------------------------------

@st.cache_resource
def load_vector_db():

    embedding = load_embedding()

    db = FAISS.load_local(

        "faiss_index",

        embedding,

        allow_dangerous_deserialization=True

    )

    return db

# ----------------------------------------------------
# Build Prompt
# ----------------------------------------------------

def build_prompt(context, question):

    prompt = f"""
You are an AI assistant for CDAC.

Answer ONLY using the given context.

If the answer is not available in the context,
reply politely with:

"I couldn't find that information in the available CDAC documents."

-------------------------

Context:

{context}

-------------------------

Question:

{question}

-------------------------

Answer:

"""

    return prompt

# ----------------------------------------------------
# Ask Question
# ----------------------------------------------------

def ask_question(question):

    db = load_vector_db()

    retriever = db.as_retriever(

        search_kwargs={"k":4}

    )

    docs = retriever.invoke(question)

    context = ""

    sources = []

    for doc in docs:

        context += doc.page_content + "\n\n"

        source = doc.metadata.get("source","Unknown File")

        page = doc.metadata.get("page","")

        sources.append(

            f"{os.path.basename(source)}  (Page {page})"

        )

    prompt = build_prompt(context, question)

    response = client.chat_completion(

        messages=[

            {

                "role":"user",

                "content":prompt

            }

        ],

        max_tokens=700,

        temperature=0.2

    )

    answer = response.choices[0].message.content

    return answer, list(set(sources))