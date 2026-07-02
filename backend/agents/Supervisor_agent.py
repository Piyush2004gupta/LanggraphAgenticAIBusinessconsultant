from models.llm import llm

def supervisor_agent(state):
    prompt = f"""You are a business supervisor. Analyze: {state.get('user_query')}
Determine which agents are needed: Market, Finance, Marketing, Legal, Risk, Strategy."""
    state["supervisor_report"] = llm.invoke(prompt).content
    return state