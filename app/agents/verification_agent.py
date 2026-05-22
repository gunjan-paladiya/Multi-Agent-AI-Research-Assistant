from langchain.schema import HumanMessage

def run_verification_agent(llm, text):

    prompt = f"""
    Verify the following content for:
    - factual accuracy
    - hallucinations
    - missing information

    Content:
    {text}
    """

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    return response.content
