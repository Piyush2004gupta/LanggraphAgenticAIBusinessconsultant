from langchain_core.tools import tool

@tool
def calculate(expression: str) -> str:
    """Perform math calculations. Example: '500000 / 12', '75 * 0.20'"""
    try:
        return f"{expression} = {eval(expression, {'__builtins__': {}}, {})}"
    except Exception as e:
        return f"Error: {e}"
