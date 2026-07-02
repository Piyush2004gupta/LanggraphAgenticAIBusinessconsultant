from langgraph.graph import StateGraph, END
from state import AgentState
from agents.Supervisor_agent import supervisor_agent
from agents.market_agent import market_agent
from agents.Finance_agent import finance_agent
from agents.marketing_agent import marketing_agent
from agents.legal_agent import legal_agent
from agents.risk_agent import risk_agent
from agents.Strategy_agent import strategy_agent
from agents.Report_agent import report_agent

workflow = StateGraph(AgentState)

workflow.add_node("Supervisor", supervisor_agent)
workflow.add_node("Market", market_agent)
workflow.add_node("Finance", finance_agent)
workflow.add_node("Marketing", marketing_agent)
workflow.add_node("Legal", legal_agent)
workflow.add_node("Risk", risk_agent)
workflow.add_node("Strategy", strategy_agent)
workflow.add_node("Report", report_agent)

workflow.set_entry_point("Supervisor")
workflow.add_edge("Supervisor", "Market")
workflow.add_edge("Market", "Finance")
workflow.add_edge("Finance", "Marketing")
workflow.add_edge("Marketing", "Legal")
workflow.add_edge("Legal", "Risk")
workflow.add_edge("Risk", "Strategy")
workflow.add_edge("Strategy", "Report")
workflow.add_edge("Report", END)

graph = workflow.compile()