from typing import TypedDict

class AgentState(TypedDict, total=False):
    user_query: str
    supervisor_report: str
    market_report: str
    finance_report: str
    marketing_report: str
    legal_report: str
    risk_report: str
    strategy_report: str
    final_report: str
