from models.llm import llm
from tools.calculator_tool import calculate
from tools.search_tool import search_web
from tools.chart_tool import create_chart
from tool_runner import run_with_tools

def finance_agent(state):
    print("\n[Finance Agent]")
    tools = [calculate, search_web, create_chart]
    prompt = f"""You are a financial analyst. Business: {state.get('user_query')}
Market Report: {state.get('market_report')}
Use calculate for revenue projections & break-even. Use create_chart for revenue chart.
Give full financial analysis with startup costs, projections Year 1-3, KPIs."""
    state["finance_report"] = run_with_tools(llm.bind_tools(tools), prompt, {t.name: t for t in tools})
    return state
