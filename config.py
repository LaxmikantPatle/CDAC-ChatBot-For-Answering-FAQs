import os
from dotenv import load_dotenv

# ======================================================
# Load Environment Variables
# ======================================================

load_dotenv()

# ======================================================
# Hugging Face Configuration
# ======================================================

HF_TOKEN = os.getenv("HF_TOKEN")

# Hugging Face LLM
LLM_MODEL = "meta-llama/Llama-3.1-8B-Instruct"

# Embedding Model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ======================================================
# Project Directories
# ======================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = os.path.join(BASE_DIR, "data")

VECTOR_DB_FOLDER = os.path.join(BASE_DIR, "faiss_index")

ASSETS_FOLDER = os.path.join(BASE_DIR, "assets")

LOGO_PATH = os.path.join(ASSETS_FOLDER, "logo.png")

# ======================================================
# Text Splitter Configuration
# ======================================================

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

# ======================================================
# Retriever Configuration
# ======================================================

TOP_K = 4

# ======================================================
# LLM Configuration
# ======================================================

TEMPERATURE = 0.2

MAX_NEW_TOKENS = 700

# ======================================================
# Streamlit Configuration
# ======================================================

PAGE_TITLE = "CDAC AI Assistant"

PAGE_ICON = "🤖"

LAYOUT = "wide"

# ======================================================
# Prompt Template
# ======================================================

SYSTEM_PROMPT = """
You are an AI assistant for CDAC.

You must answer ONLY from the provided context.

Rules:

1. Never make up answers.

2. If the answer is not found in the context,
   say:

   "I couldn't find that information in the available CDAC documents."

3. Keep answers clear and professional.

4. If the question is unrelated to CDAC,
   politely say that you can answer only
   CDAC-related questions.

5. Use bullet points whenever appropriate.
"""