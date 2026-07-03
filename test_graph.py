import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "backend"))

from backend.graph import graph

if __name__ == "__main__":
    print("Testing LangGraph Dynamic Routing...")
    initial_state = {"user_query": "What are the legal risks of opening a crypto exchange in India?"}
    try:
        result = graph.invoke(initial_state)
        print("\n=== SUPERVISOR DECISION ===")
        print(f"Routing to: {result.get('next_agent')}")
        print(f"Reasoning: {result.get('supervisor_report')}")
        
        print("\n=== FINAL REPORT ===")
        print(result.get("final_report", "No report generated."))
    except Exception as e:
        print(f"Error: {e}")
