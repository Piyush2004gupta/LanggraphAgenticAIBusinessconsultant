import os, sys
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
sys.path.append(os.path.dirname(__file__))

from graph import graph
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import answer_relevancy, faithfulness, context_precision

question = "What are the legal risks of opening a crypto exchange in India?"
answer = graph.invoke({"user_query": question}).get("final_report", "")

dataset = Dataset.from_dict({
    "question": [question],
    "answer": [answer],
    "contexts": [["Crypto rules in India are strict."]],
    "ground_truth": ["Significant regulatory uncertainty and strict taxation laws apply."]
})

print(evaluate(dataset, metrics=[answer_relevancy, faithfulness, context_precision]))
