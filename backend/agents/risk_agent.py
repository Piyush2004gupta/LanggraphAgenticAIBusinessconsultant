from models.llm import llm
from tools.search_tool import search_web
from tools.calculator_tool import calculate
from tool_runner import run_with_tools

def risk_agent(state):
    tools = [search_web, calculate]
    prompt = f"""You are a risk analyst. 
Market: {state.get('market_report')} | Finance: {state.get('finance_report')}
Use search_web to research industry risks and failures.
Identify: Operational, Competition, Financial, Technical, Regulatory risks with ratings (High/Medium/Low) and mitigations."""
    state["risk_report"] = run_with_tools(llm.bind_tools(tools), prompt, {t.name: t for t in tools})
    return state