from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

# STEP 1: Load extracted text
with open("extracted_output.txt", "r", encoding="utf-8") as f:
    text = f.read()

# STEP 2: Split text into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_text(text)
documents = [Document(page_content=chunk) for chunk in chunks]

# STEP 3: Create embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# STEP 4: Build FAISS vectorstore
vectorstore = FAISS.from_documents(documents, embedding_model)

# STEP 5: Save it
vectorstore.save_local("faiss_index")

print(" FAISS index created.")
