from models.llm import llm
from tools.search_tool import search_web
from tool_runner import run_with_tools

def marketing_agent(state):
    tools = [search_web]
    prompt = f"""You are a marketing strategist. Business: {state.get('user_query')}
Use search_web to research best marketing channels and competitor strategies.
Give full marketing plan: Instagram, Google Ads, SEO, Email, Branding."""
    state["marketing_report"] = run_with_tools(llm.bind_tools(tools), prompt, {t.name: t for t in tools})
    return state