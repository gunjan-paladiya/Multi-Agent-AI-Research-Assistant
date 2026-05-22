from langchain.schema import HumanMessage

def run_report_agent(llm, text):

    prompt = f"""
    Create a professional research report.

    Content:
    {text}

    Include:
    - Introduction
    - Key Findings
    - Insights
    - Conclusion
    """

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    return response.content
