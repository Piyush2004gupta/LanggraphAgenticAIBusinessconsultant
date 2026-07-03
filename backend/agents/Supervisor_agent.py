from models.llm import llm
from pydantic import BaseModel, Field
from typing import Literal

class RoutingDecision(BaseModel):
    reasoning: str = Field(description="Why you chose this agent")
    next_agent: Literal["Market", "Finance", "Marketing", "Legal", "Risk", "Strategy", "Report"] = Field(
        description="The next agent to route the task to"
    )

def supervisor_agent(state):
    query = state.get("user_query")
    prompt = f"""You are a business supervisor. Analyze the following request: '{query}'
Your job is to route this request to the single most appropriate specialist agent:
- Market: For market research, competitors, trends.
- Finance: For financial analysis, budgets, investments.
- Marketing: For marketing strategies, campaigns, SEO.
- Legal: For compliance, lawsuits, regulations, terms.
- Risk: For risk assessment, mitigation plans.
- Strategy: For overall business strategy, growth, pivots.
- Report: If the request is a general summary and doesn't need a specialist.

Select the BEST single agent to handle this request initially."""

    structured_llm = llm.with_structured_output(RoutingDecision)
    decision = structured_llm.invoke(prompt)
    
    state["supervisor_report"] = decision.reasoning
    state["next_agent"] = decision.next_agent
    return state