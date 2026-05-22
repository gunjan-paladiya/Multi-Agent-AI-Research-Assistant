from langchain.schema import HumanMessage

def run_summary_agent(llm, text):

    prompt = f"""
    Summarize the following content:

    {text}
    """

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    return response.content
