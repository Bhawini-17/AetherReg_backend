from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

# Update with the path to your PDF
PDF_PATH = "docs/rbi_circular.pdf"

# Step 1: Load the PDF
loader = PyPDFLoader(PDF_PATH)
documents = loader.load()

# Step 2: Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
docs = text_splitter.split_documents(documents)

# Step 3: Create Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Step 4: Store vectors in FAISS
vectorstore = FAISS.from_documents(docs, embeddings)

# Step 5: Save index locally
vectorstore.save_local("faiss_index")
print("Document indexed and saved to 'faiss_index'")
