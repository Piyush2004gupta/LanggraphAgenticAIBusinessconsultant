from typing import TypedDict, Annotated, Sequence
import operator

class AgentState(TypedDict):
    user_query: str
    next_agent: str
    supervisor_report: str
    market_report: str
    finance_report: str
    marketing_report: str
    legal_report: str
    risk_report: str
    strategy_report: str
    final_report: str