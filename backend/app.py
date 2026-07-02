import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from graph import graph

def run_business_analysis(user_query: str):
    print("\n" + "="*60)
    print("LANGGRAPH AGENTIC AI - BUSINESS ANALYZER")
    print("="*60)
    print(f"Analyzing: {user_query}\n")

    initial_state = {"user_query": user_query}
    result = graph.invoke(initial_state)

    print("\n" + "="*60)
    print("FINAL BUSINESS REPORT")
    print("="*60)
    print(result.get("final_report", "No report generated."))
    print("="*60)

    return result

if __name__ == "__main__":
    # Change this query to test different business ideas
    query = "Online food delivery startup in India"
    run_business_analysis(query)