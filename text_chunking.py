from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# Step 1: Load extracted text from file
loader = TextLoader("extracted_output.txt")
documents = loader.load()

# Step 2: Split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

# Step 3: Generate embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Step 4: Create and store in FAISS
vectorstore = FAISS.from_documents(docs, embeddings)
vectorstore.save_local("faiss_index")

print("Text chunked, embedded, and stored in FAISS!")
