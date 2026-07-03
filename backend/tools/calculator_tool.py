from langchain_core.tools import Tool

def calculate(expression: str):
    return str(eval(expression))

calculator_tool = Tool(
    name="Calculator",
    func=calculate,
    description="Perform mathematical calculations."
)