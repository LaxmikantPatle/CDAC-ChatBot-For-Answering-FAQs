# 🤖 CDAC FAQ Chatbot — RAG-Based Question Answering System

An intelligent **FAQ Question-Answering Chatbot** built as a CDAC PG Diploma project using **Retrieval-Augmented Generation (RAG)**.

The application uses **LangChain, Hugging Face, FAISS, and Streamlit** to retrieve relevant information from a knowledge base and generate context-aware answers to user questions.

🔗 **Live Demo:**  
https://cdac-chatbot-for-answering-faqs.streamlit.app/

🔗 **GitHub Repository:**  
https://github.com/LaxmikantPatle/CDAC-ChatBot-For-Answering-FAQs

---

## 📌 Project Overview

Traditional FAQ systems generally depend on exact keyword matching or predefined responses. This project takes a more intelligent approach by combining **semantic search** with **Retrieval-Augmented Generation (RAG)**.

Instead of expecting the user to ask a question exactly as it appears in the FAQ dataset, the system:

1. Receives the user's question.
2. Converts the question into an embedding.
3. Searches the FAISS vector database for semantically relevant information.
4. Retrieves the most relevant context.
5. Provides that context to the language model.
6. Generates an appropriate answer based on the retrieved information.

### High-Level Architecture

```text
                    ┌───────────────────┐
                    │     User Query    │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │    Streamlit UI   │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │  Query Processing │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Text Embeddings   │
                    │  Hugging Face     │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   FAISS Vector    │
                    │      Search       │
                    └─────────┬─────────┘
                              │
                       Relevant Context
                              │
                              ▼
                    ┌───────────────────┐
                    │       RAG         │
                    │ Retrieval + LLM   │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Generated Answer  │
                    └───────────────────┘
```

---

## ✨ Key Features

### 🧠 Retrieval-Augmented Generation

The chatbot combines retrieval and generation instead of relying solely on a language model.

```text
Question
   ↓
Semantic Retrieval
   ↓
Relevant Context
   ↓
Language Model
   ↓
Answer
```

This helps the chatbot answer questions using information from the project's knowledge base.

### 🔎 Semantic Search

The system uses vector embeddings to understand the semantic meaning of a question rather than relying only on exact keyword matching.

For example:

```text
"What courses does CDAC offer?"
```

and:

```text
"Which programs are available at CDAC?"
```

can potentially retrieve related information even though the wording is different.

### 🗂️ FAISS Vector Database

FAISS is used for efficient similarity search over vector embeddings.

The repository contains a dedicated:

```text
faiss_index/
```

directory for the vector index.

### 🤗 Hugging Face

Hugging Face components are used as part of the NLP/embedding and inference stack.

### 🦜🔗 LangChain

LangChain provides the components required to build the retrieval and question-answering pipeline.

### 🎨 Streamlit Interface

The chatbot is exposed through an interactive Streamlit web application.

### 📚 Knowledge-Base Driven Answers

The system is designed to answer questions based on the information available in its knowledge base rather than functioning as a completely unrestricted general-purpose chatbot.

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Application development |
| 🎨 Streamlit | Web interface |
| 🦜🔗 LangChain | RAG pipeline and orchestration |
| 🤗 Hugging Face | NLP models / embeddings / inference |
| 🔎 FAISS | Vector similarity search |
| 📄 PDF/Data Processing | Knowledge-base preparation |
| 🔤 Embeddings | Semantic representation of text |
| ☁️ Streamlit Cloud | Application deployment |

The GitHub repository is explicitly tagged with **FAISS, Hugging Face, LangChain, Python, RAG, and Streamlit**.

---

# 📂 Project Structure

```text
CDAC-ChatBot-For-Answering-FAQs/
│
├── .streamlit/
│   └── Streamlit configuration
│
├── Data/
│   └── Knowledge-base / project data
│
├── assets/
│   └── Application assets
│
├── faiss_index/
│   └── FAISS vector database/index
│
├── app.py
│   └── Streamlit application entry point
│
├── create_vector_db.py
│   └── Creates/builds the vector database
│
├── rag.py
│   └── RAG retrieval and question-answering logic
│
├── requirements.txt
│   └── Python dependencies
│
├── runtime.txt
│   └── Python runtime configuration
│
└── .gitignore
```

This structure reflects the files currently visible in the repository.

---

# 🔄 RAG Pipeline

The core concept behind the application is **Retrieval-Augmented Generation**.

## Step 1 — Knowledge Base

Relevant FAQ/document information is collected and prepared as the chatbot's knowledge source.

```text
Documents / FAQs
       ↓
Text Extraction
       ↓
Text Processing
```

## Step 2 — Create Embeddings

The text is converted into numerical vector representations using an embedding model.

```text
Text
 ↓
Embedding Model
 ↓
Vector Representation
```

## Step 3 — Build FAISS Index

The generated vectors are stored in a FAISS index.

```text
Document Vectors
       ↓
   FAISS Index
       ↓
Similarity Search
```

The repository contains the generated `faiss_index` directory.

## Step 4 — User Question

The user enters a question through the Streamlit application.

```text
User Question
      ↓
Question Embedding
```

## Step 5 — Retrieval

The question vector is compared against the stored vectors.

```text
Question Vector
      ↓
FAISS Similarity Search
      ↓
Top Relevant Documents
```

## Step 6 — Generation

The retrieved context is passed into the RAG pipeline to generate the final answer.

```text
Question
   +
Retrieved Context
   ↓
Language Model
   ↓
Final Answer
```

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/LaxmikantPatle/CDAC-ChatBot-For-Answering-FAQs.git
```

Move into the project directory:

```bash
cd CDAC-ChatBot-For-Answering-FAQs
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Build the Vector Database

If you are creating the FAISS index from the source knowledge base, run:

```bash
python create_vector_db.py
```

This project includes `create_vector_db.py` specifically for vector-database creation.

---

## 5. Run the Streamlit Application

```bash
streamlit run app.py
```

The application should then be available locally through the Streamlit URL displayed in your terminal.

---

# 💬 Example Workflow

A typical interaction looks like:

```text
User
 │
 │  "What is CDAC?"
 ▼
Streamlit Chat Interface
 │
 ▼
Question Embedding
 │
 ▼
FAISS Similarity Search
 │
 ▼
Relevant FAQ / Document Context
 │
 ▼
RAG Pipeline
 │
 ▼
AI Generated Answer
```

---

# ☁️ Deployment

The project is deployed using **Streamlit Cloud**.

### Live Application

👉 https://cdac-chatbot-for-answering-faqs.streamlit.app/

The GitHub repository currently links to this Streamlit application.

To deploy your own version:

1. Fork or clone the repository.
2. Push the project to GitHub.
3. Open Streamlit Community Cloud.
4. Connect your GitHub repository.
5. Select:

```text
app.py
```

as the main application file.
6. Deploy the application.

---

# 🔐 Environment Variables / Secrets

If the configured Hugging Face inference provider requires authentication, the Hugging Face API token should be stored securely as a Streamlit secret.

Do **not** hard-code API keys in:

```text
app.py
```

or:

```text
requirements.txt
```

For Streamlit Cloud, configure secrets through the application's **Secrets** settings.

Example:

```toml
HF_TOKEN = "your_huggingface_token"
```

Use the exact environment variable name expected by your application code.

---

# ⚙️ Requirements

The project uses a Python dependency file:

```text
requirements.txt
```

and also includes:

```text
runtime.txt
```

for runtime configuration.

The main technology dependencies include:

```text
streamlit
langchain
langchain-community
langchain-text-splitters
faiss-cpu
sentence-transformers
huggingface-hub
pypdf
python-dotenv
transformers
torch
accelerate
einops
```

Keep the versions in `requirements.txt` synchronized with the Python runtime used for deployment.

---

# 🧪 Testing the Chatbot

Test the application using questions that are directly related to the information contained in the knowledge base.

### Example test categories

| Category | Example |
|---|---|
| General FAQ | "What is CDAC?" |
| Courses | "What courses are available?" |
| Admission | "How can I apply?" |
| Eligibility | "What are the eligibility requirements?" |
| Program Information | "Tell me about the course." |

The quality of the answer depends heavily on the quality and coverage of the underlying knowledge base.

---

# 🧩 Core Components

## `app.py`

The main Streamlit application.

Responsible for the user-facing chatbot interface and application execution.

## `rag.py`

Contains the Retrieval-Augmented Generation functionality.

The RAG layer connects the user's question with relevant retrieved information before generating an answer.

## `create_vector_db.py`

Responsible for creating the vector database/index from the project's source information.

## `faiss_index/`

Contains the FAISS vector index used for similarity-based retrieval.

## `Data/`

Contains the project's knowledge/data resources.

## `assets/`

Contains application-related assets.

---

# 📐 System Design

```text
             ┌─────────────────────┐
             │   Knowledge Base    │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Text Processing     │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Embedding Model     │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │   FAISS Index       │
             └──────────┬──────────┘
                        │
                        │
User ──────► Question ──┤
                        │
                        ▼
             ┌─────────────────────┐
             │ Similarity Retrieval│
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Retrieved Context   │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │       RAG           │
             │  Language Model     │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │   Final Answer      │
             └─────────────────────┘
```

---

# 🎯 Project Objectives

The project demonstrates practical implementation of:

- Retrieval-Augmented Generation
- Semantic search
- Vector databases
- Text embeddings
- Question answering
- LangChain pipelines
- Hugging Face models
- FAISS similarity search
- Streamlit application development
- AI application deployment

---

# ⚠️ Limitations

The chatbot's answers depend on the information available in its knowledge base.

If relevant information cannot be retrieved, the system may not be able to provide a reliable answer.

Other practical limitations may include:

- Embedding quality
- Retrieval quality
- Knowledge-base completeness
- Language-model limitations
- API/inference availability
- Computational resources
- Large vector-index loading time

---

# 🔮 Future Improvements

Potential improvements include:

### 🔎 Better Retrieval

- Hybrid keyword + semantic search
- Re-ranking retrieved documents
- Improved chunking strategies
- Metadata filtering

### 🧠 Better Generation

- Improved LLM selection
- Prompt optimization
- Context-window optimization
- Hallucination reduction

### 💬 Conversation Memory

Add conversational context so users can ask follow-up questions such as:

```text
User: What courses are available?

Bot: ...

User: What is the eligibility for that course?
```

### 📊 Evaluation

Add automated RAG evaluation using metrics such as:

- Retrieval Precision
- Retrieval Recall
- Context Relevance
- Answer Relevance
- Faithfulness

### 🛡️ Safety

Add safeguards for unsupported or inappropriate queries and ensure that answers remain grounded in the knowledge base.

---

# 🏆 Skills Demonstrated

This project demonstrates hands-on experience with:

```text
Python
   │
   ├── NLP
   ├── Embeddings
   ├── Semantic Search
   ├── RAG
   ├── Vector Databases
   ├── LangChain
   ├── Hugging Face
   ├── FAISS
   └── Streamlit
```

---

# 👨‍💻 Author

## Laxmikant Patle

CDAC PG Diploma Project

GitHub:  
https://github.com/LaxmikantPatle

---

# ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project was created as part of a CDAC PG Diploma project.

Add an appropriate open-source license to the repository if you intend to distribute or modify the project publicly.