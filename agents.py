from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import Ollama
from utils import check_risks

# Initialize OLLAMA LLM
llm = Ollama(model="llama3.2:1b")  # or any local HuggingFace LLM

# Summarization agent
summary_prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following contract text clearly and concisely:\n{text}"
)
summary_chain = LLMChain(llm=llm, prompt=summary_prompt)

# Clause identification agent
clause_prompt = PromptTemplate(
    input_variables=["text"],
    template="Identify key clauses in this contract text and categorize them (e.g., termination, liability, confidentiality):\n{text}"
)
clause_chain = LLMChain(llm=llm, prompt=clause_prompt)

def process_contract(text_chunks):
    results = []
    for chunk in text_chunks:
        summary = summary_chain.run(chunk)
        clauses = clause_chain.run(chunk)
        risks = check_risks(chunk)
        results.append({
            "text": chunk,
            "summary": summary,
            "clauses": clauses,
            "risks": risks
        })
    return results
