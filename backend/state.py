from typing import TypedDict
class AgentState(TypedDict):
    user_query: str
    supervisor_agent: str
    market_agent: str
    finance_agent: str
    marketing_agent: str
    legal_agent: str
    risk_agent: str
    strategy_agent: str
    final_agent: str