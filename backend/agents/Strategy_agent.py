from models.llm import llm
from tools.search_tool import search_web
from tool_runner import run_with_tools

def strategy_agent(state):
    print("\n[Strategy Agent]")
    tools = [search_web]
    prompt = f"""You are a business strategist.
Market: {state.get('market_report')} | Finance: {state.get('finance_report')}
Risk: {state.get('risk_report')}
Use search_web to research successful strategies in this industry.
Create: Business Roadmap, Quarterly Goals, Growth Plan, Expansion Plan, KPIs."""
    state["strategy_report"] = run_with_tools(llm.bind_tools(tools), prompt, {t.name: t for t in tools})
    return state
