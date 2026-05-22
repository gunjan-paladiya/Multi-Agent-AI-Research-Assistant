from typing import TypedDict
from langgraph.graph import StateGraph, END

class AgentState(TypedDict):

    query: str
    research: str
    summary: str
    verification: str
    report: str

def build_graph(
    research_node,
    summary_node,
    verification_node,
    report_node
):

    workflow = StateGraph(AgentState)

    workflow.add_node("ResearchAgent", research_node)
    workflow.add_node("SummaryAgent", summary_node)
    workflow.add_node("VerificationAgent", verification_node)
    workflow.add_node("ReportAgent", report_node)

    workflow.set_entry_point("ResearchAgent")

    workflow.add_edge("ResearchAgent", "SummaryAgent")
    workflow.add_edge("SummaryAgent", "VerificationAgent")
    workflow.add_edge("VerificationAgent", "ReportAgent")
    workflow.add_edge("ReportAgent", END)

    return workflow.compile()
