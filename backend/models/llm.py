import os
import yaml
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Load model versioning configuration
config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yml")
model_name = "gpt-4o-mini" # default fallback
if os.path.exists(config_path):
    with open(config_path, "r") as f:
        try:
            config = yaml.safe_load(f)
            for m in config.get("models", []):
                if m.get("type") == "main":
                    model_name = m.get("model", "gpt-4o-mini")
                    break
        except Exception as e:
            print(f"Error loading config.yml: {e}")

llm = ChatOpenAI(
    model=model_name,
    api_key=os.getenv("OPENAI_API_KEY")
)
