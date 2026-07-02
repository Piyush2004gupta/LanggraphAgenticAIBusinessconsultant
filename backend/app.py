import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from graph import graph

def run_business_analysis(user_query: str):
    initial_state = {"user_query": user_query}
    result = graph.invoke(initial_state)
    return result

if __name__ == "__main__":
    # Change this query to test different business ideas
    query = "Online food delivery startup in India"
    run_business_analysis(query)