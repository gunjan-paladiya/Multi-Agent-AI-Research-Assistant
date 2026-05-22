from fastapi import APIRouter
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

from app.database.vector_store import build_vector_store
from app.agents.research_agent import run_research_agent
from app.agents.summarization_agent import run_summary_agent
from app.agents.verification_agent import run_verification_agent
from app.agents.report_agent import run_report_agent

router = APIRouter()

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.2
)

vectorstore = build_vector_store()

retriever = vectorstore.as_retriever()

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

@router.post("/research")
def research(query: str):

    research = run_research_agent(
        query,
        qa_chain
    )

    summary = run_summary_agent(
        llm,
        research
    )

    verification = run_verification_agent(
        llm,
        summary
    )

    report = run_report_agent(
        llm,
        verification
    )

    return {
        "query": query,
        "report": report
    }
