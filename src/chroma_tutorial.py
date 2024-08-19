# import
from pydoc import doc
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_text_splitters import CharacterTextSplitter
import sympy as sp

# load the document and split it into chunks
loader = TextLoader("../BindInjection.txt")
documents = loader.load()

# split it into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0) 
docs = text_splitter.split_documents(documents)

import chromadb

embeddings = OpenAIEmbeddings()

# load it into Chroma
db = Chroma.from_documents(docs, embeddings)

# query it
query = "How to inject queries with side effects?"

# create simple ids
ids = [str(i) for i in range(1, len(docs) + 1)]

# add data
example_db = Chroma.from_documents(docs, embeddings, ids=ids)
docs = example_db.similarity_search(query)
print(docs[0].metadata)

# update the metadata for a document
docs[0].metadata = {
    "source": "../state_of_the_union.txt",
    "new_value": "hello world",
}
example_db.update_document(ids[0], docs[0])
print(example_db._collection.get(ids=[ids[0]]))
print(example_db._collection.get(ids=[ids[1]]))

# delete the last document
print("count before", example_db._collection.count())

example_db._collection.delete(ids=[ids[-1]])
print("count after", example_db._collection.count())

