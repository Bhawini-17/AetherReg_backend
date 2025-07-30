from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama  # <-- using local model
# If you prefer OpenAI instead, uncomment below
# from langchain_openai import OpenAI

from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

# Step 1: Load FAISS vectorstore
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# Step 2: Set up the retriever
retriever = vectorstore.as_retriever()

# Step 3: Define your custom prompt
custom_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a compliance expert AI. Given the context below, answer the user's question clearly.

Context: {context}

Question: {question}

Answer:"""
)

# Step 4: Load QA chain with a local model (LLaMA3)
llm = Ollama(
    model="llama3", 
    temperature=0,  # limit output length to prevent infinite text
)

# If you're using OpenAI instead of Ollama:
# llm = OpenAI(temperature=0, max_tokens=500, openai_api_key="YOUR_KEY")

qa_chain = load_qa_chain(llm, chain_type="stuff", prompt=custom_prompt)

# Step 5: Ask your question
while True:
    query = input("\nAsk a question (or type 'exit'): ")
    if query.lower() == "exit":
        break
    docs = retriever.get_relevant_documents(query)
    answer = qa_chain.invoke({"input_documents": docs, "question": query})
    print(f"\nAnswer: {answer}")
