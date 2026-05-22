from langchain.chains import RetrievalQA

def run_research_agent(query, qa_chain: RetrievalQA):
    result = qa_chain.run(query)
    return result
