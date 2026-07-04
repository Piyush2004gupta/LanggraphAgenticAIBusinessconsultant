import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from graph import graph
# pyrefly: ignore [missing-import]
from nemoguardrails import LLMRails, RailsConfig
from langfuse.callback import CallbackHandler
from langchain.globals import set_llm_cache
from langchain_community.cache import RedisCache
from langchain_community.callbacks.manager import get_openai_callback
from redis import Redis

# Set up Redis caching for Langchain LLMs
set_llm_cache(RedisCache(redis_=Redis.from_url("redis://localhost:6379")))

config = RailsConfig.from_path("config")
rails = LLMRails(config)
langfuse_handler = CallbackHandler()

app = FastAPI()

# Enable CORS so the frontend can hit this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

@app.post("/api/analyze")
async def analyze_business(request: QueryRequest):
    initial_state = {"user_query": request.query}
    
    with get_openai_callback() as cb:
        result = graph.invoke(initial_state, config={"callbacks": [langfuse_handler]})
        
        print(f"\n--- Cost Tracking ---")
        print(f"Total Tokens: {cb.total_tokens}")
        print(f"Prompt Tokens: {cb.prompt_tokens}")
        print(f"Completion Tokens: {cb.completion_tokens}")
        print(f"Total Cost (USD): ${cb.total_cost:.4f}")
        print(f"---------------------\n")
    
    # Return the final report if it exists, otherwise a summary of the state
    final_report = result.get("final_report", "Analysis completed but no final report was generated.")
    return {"response": final_report}

@app.get("/api/download/{filename}")
async def download_file(filename: str):
    file_path = os.path.join(os.getcwd(), filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, filename=filename)
    return {"error": "File not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
