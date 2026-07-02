from langchain_core.tools import tool
import os

@tool
def save_report(text: str, filename: str = "business_report.txt") -> str:
    """Save the business report as a text file."""
    path = os.path.join(os.getcwd(), filename)
    open(path, "w", encoding="utf-8").write(text)
    return f"Saved to: {path}"