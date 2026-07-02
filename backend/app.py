from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from graph import graph

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
    result = graph.invoke(initial_state)
    
    # Return the final report if it exists, otherwise a summary of the state
    final_report = result.get("final_report", "Analysis completed but no final report was generated.")
    return {"response": final_report}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)