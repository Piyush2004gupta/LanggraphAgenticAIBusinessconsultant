from models.llm import llm
from tools.search_tool import search_web
from tools.web_scraper import scrape_website
from tool_runner import run_with_tools

def market_agent(state):
    tools = [search_web, scrape_website]
    prompt = f"""You are a market analyst. Business: {state.get('user_query')}
Use search_web to research market size, competitors, and trends.
Give a full market analysis."""
    state["market_report"] = run_with_tools(llm.bind_tools(tools), prompt, {t.name: t for t in tools})
    return state