import getpass
import os

# os.environ["OPENAI_API_KEY"] = getpass.getpass()
os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

# create and query vector stores
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

# Load the document, split it into chunks, embed each chunk and load it into the vector store.
raw_documents_guide = TextLoader('../dataset/txt/SQLInjectionStrategies.txt').load()
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents_guide)

# uses the chroma vector database, which runs on your local machine as a library.
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

vectorstore = Chroma.from_documents(
    documents,
    embedding=OpenAIEmbeddings(),
)

from typing import List

from langchain_core.documents import Document
from langchain_core.runnables import RunnableLambda

retriever = RunnableLambda(vectorstore.similarity_search).bind(k=1)  # select top 1 result

# retriever.batch(["cat", "shark"])

#Call the retriever with a query
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

message = """
Answer this question using the provided context only.

{question}

Context:
{context}
"""

prompt = ChatPromptTemplate.from_messages([("human", message)])

rag_chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | llm


def ask_question(question: str):
    response = rag_chain.invoke("tell me about cats")
    print(response.content)



