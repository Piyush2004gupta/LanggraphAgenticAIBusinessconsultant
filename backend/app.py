from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from graph import graph
import os

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

@app.get("/api/download/{filename}")
async def download_file(filename: str):
    file_path = os.path.join(os.getcwd(), filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, filename=filename)
    return {"error": "File not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)