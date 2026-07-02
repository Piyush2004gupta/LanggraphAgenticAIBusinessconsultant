from models.llm import llm
from tools.search_tool import search_web
from tool_runner import run_with_tools

def legal_agent(state):
    print("\n[Legal Agent]")
    tools = [search_web]
    prompt = f"""You are a legal advisor for India. Business: {state.get('user_query')}
Use search_web to research required licenses, GST, and compliance in India.
Suggest: FSSAI, GST, Business Registration type, Legal Compliance Checklist."""
    state["legal_report"] = run_with_tools(llm.bind_tools(tools), prompt, {t.name: t for t in tools})
    return state
