import os

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# ==========================================================
# Load Environment Variables
# ==========================================================

# ==========================================================
# Folder Paths
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = os.path.join(BASE_DIR, "Data")      # Change to "data" if needed
VECTOR_DB_FOLDER = os.path.join(BASE_DIR, "faiss_index")

# ==========================================================
# Check Data Folder
# ==========================================================

print("=" * 60)
print("Current Directory :", BASE_DIR)
print("Data Folder       :", DATA_FOLDER)
print("=" * 60)

if not os.path.exists(DATA_FOLDER):
    raise FileNotFoundError(f"Data folder not found:\n{DATA_FOLDER}")

files = os.listdir(DATA_FOLDER)

print("Files Found:")
print(files)
print("=" * 60)

# ==========================================================
# Load TXT Files
# ==========================================================

documents = []

for file in files:

    if not file.lower().endswith(".txt"):
        continue

    file_path = os.path.join(DATA_FOLDER, file)

    print(f"Loading: {file}")

    try:

        loader = TextLoader(
            file_path,
            encoding="utf-8",
            autodetect_encoding=True
        )

        docs = loader.load()

        for doc in docs:

            # Skip empty files
            if doc.page_content.strip():

                doc.metadata["source"] = file

                documents.append(doc)

        print(f"Loaded Successfully: {file}")

    except Exception as e:

        print(f"Error loading {file}")
        print(e)

print("\nTotal Documents Loaded:", len(documents))

# ==========================================================
# Stop if no documents
# ==========================================================

if len(documents) == 0:

    raise Exception(
        "No text documents were loaded.\n"
        "Check that:\n"
        "1. Files are inside the Data folder\n"
        "2. Files have .txt extension\n"
        "3. Files are not empty"
    )

# ==========================================================
# Split Documents
# ==========================================================

print("\nSplitting Documents...")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print("Total Chunks:", len(chunks))

if len(chunks) == 0:
    raise Exception("No chunks were created.")

# ==========================================================
# Load Embedding Model
# ==========================================================

print("\nLoading Embedding Model...")

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding Model Loaded")

# ==========================================================
# Create FAISS Database
# ==========================================================

print("\nCreating FAISS Vector Database...")

vector_db = FAISS.from_documents(
    chunks,
    embedding
)

# ==========================================================
# Save FAISS
# ==========================================================

os.makedirs(VECTOR_DB_FOLDER, exist_ok=True)

vector_db.save_local(VECTOR_DB_FOLDER)

print("\n" + "=" * 60)
print("FAISS Index Created Successfully")
print("Saved To:", VECTOR_DB_FOLDER)
print("=" * 60)