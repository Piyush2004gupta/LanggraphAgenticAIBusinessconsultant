import os
import sys
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
sys.path.append(os.path.dirname(__file__))

from graph import graph
from langsmith import Client
from langsmith.evaluation import evaluate, LangChainStringEvaluator

def predict(inputs: dict) -> dict:
    """Wrapper function to pass to LangSmith evaluator."""
    result = graph.invoke({"user_query": inputs["question"]})
    return {"answer": result.get("final_report", "")}

def run_prompt_evaluation():
    client = Client()
    
    # 1. Create a dataset in LangSmith (or use existing)
    dataset_name = "Business Analysis Prompts"
    if not client.has_dataset(dataset_name=dataset_name):
        dataset = client.create_dataset(
            dataset_name=dataset_name,
            description="Dataset for testing business query prompt performance."
        )
        # Add examples
        examples = [
            ("What are the legal risks of opening a crypto exchange in India?", 
             "Significant regulatory uncertainty and strict taxation laws apply."),
            ("What is a good marketing strategy for a new SaaS product?", 
             "Content marketing, SEO, and targeted LinkedIn ads.")
        ]
        for q, a in examples:
            client.create_example(
                inputs={"question": q},
                outputs={"expected_answer": a},
                dataset_id=dataset.id,
            )
    
    # 2. Define evaluators (e.g., QA correctness)
    qa_evaluator = LangChainStringEvaluator("qa")
    
    print(f"Running LangSmith evaluation on dataset: {dataset_name}...")
    
    # 3. Run evaluation
    results = evaluate(
        predict,
        data=dataset_name,
        evaluators=[qa_evaluator],
        experiment_prefix="prompt-eval-run",
    )
    
    print("\nEvaluation complete! Check your LangSmith dashboard for the detailed score report.")

if __name__ == "__main__":
    run_prompt_evaluation()
