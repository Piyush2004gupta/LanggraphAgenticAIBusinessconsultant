from models.llm import llm
from tools.file_tool import save_report
from tools.pdf_tool import save_pdf
from tool_runner import run_with_tools

def report_agent(state):
    tools = [save_report, save_pdf]
    prompt = f"""You are a report writer. Create a professional business report.
Supervisor Context: {state.get('supervisor_report')}
Market: {state.get('market_report')} | Finance: {state.get('finance_report')}
Marketing: {state.get('marketing_report')} | Legal: {state.get('legal_report')}
Risk: {state.get('risk_report')} | Strategy: {state.get('strategy_report')}
Use save_report to save as TXT and save_pdf to save as PDF.
Include: Executive Summary, all sections, Conclusion & Next Steps."""
    state["final_report"] = run_with_tools(llm.bind_tools(tools), prompt, {t.name: t for t in tools})
    return state
