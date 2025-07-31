import os
import pdfplumber
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# 1. Load PDF and extract text
def load_pdf_text(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# 2. Convert text into Document chunks
def split_text_into_docs(text):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return [Document(page_content=chunk) for chunk in text_splitter.split_text(text)]

# 3. Create vector store with FAISS
def create_vector_store(documents):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.from_documents(documents, embeddings)

# 4. Load local LLM (FLAN-T5)
def load_local_llm():
    model_name = "google/flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer, max_length=512)
    return HuggingFacePipeline(pipeline=pipe)

# 5. Main query function
def main():
    pdf_path = "docs/rbi_circular.pdf"  # replace with your PDF
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"{pdf_path} not found!")

    raw_text = load_pdf_text(pdf_path)
    documents = split_text_into_docs(raw_text)
    vectorstore = create_vector_store(documents)
    retriever = vectorstore.as_retriever()

    llm = load_local_llm()
    qa_chain = load_qa_chain(llm, chain_type="stuff")

    while True:
        query = input("Ask your question (or type 'exit'): ")
        if query.lower() == 'exit':
            break
        docs = retriever.get_relevant_documents(query)
        result = qa_chain.run(input_documents=docs, question=query)
        print(f"\nAnswer: {result}\n")

if __name__ == "__main__":
    main()
