import os

# os.environ["OPENAI_API_KEY"] = getpass.getpass()
os.environ["OPENAI_API_KEY"] = "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"

from langchain_openai import ChatOpenAI

from langchain_community.document_loaders import TextLoader

from langchain.chains.summarize import load_summarize_chain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate

def summarize_context(loop_count):
    # Define prompt
    prompt_template = """Write a concise summary of the following:
    "{text}"
    CONCISE SUMMARY:"""

    prompt = PromptTemplate.from_template(prompt_template)

    # Define LLM chain
    llm = ChatOpenAI(temperature=0, model="gpt-4o")
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    chain = load_summarize_chain(llm, chain_type="stuff")

    # Load context documents
    current_loop_context_docs = TextLoader(f"../session/sqlmap_out/loop_{loop_count}.txt").load()
    
    print(chain.invoke(current_loop_context_docs)["output_text"])




