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

def route_from_supervisor(state):
    return state.get("next_agent", "Report")

workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("Supervisor", supervisor_agent)
workflow.add_node("Market", market_agent)
workflow.add_node("Finance", finance_agent)
workflow.add_node("Marketing", marketing_agent)
workflow.add_node("Legal", legal_agent)
workflow.add_node("Risk", risk_agent)
workflow.add_node("Strategy", strategy_agent)
workflow.add_node("Report", report_agent)

# Set Entry Point
workflow.set_entry_point("Supervisor")

# Add Conditional Edges from Supervisor
workflow.add_conditional_edges(
    "Supervisor",
    route_from_supervisor,
    {
        "Market": "Market",
        "Finance": "Finance",
        "Marketing": "Marketing",
        "Legal": "Legal",
        "Risk": "Risk",
        "Strategy": "Strategy",
        "Report": "Report"
    }
)

# All sub-agents always route to the Report agent when they finish
workflow.add_edge("Market", "Report")
workflow.add_edge("Finance", "Report")
workflow.add_edge("Marketing", "Report")
workflow.add_edge("Legal", "Report")
workflow.add_edge("Risk", "Report")
workflow.add_edge("Strategy", "Report")

# The Report agent finishes the workflow
workflow.add_edge("Report", END)

graph = workflow.compile()