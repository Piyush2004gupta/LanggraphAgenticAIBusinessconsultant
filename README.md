# LangGraph Agentic AI - Business Consultant

An AI-powered business consultant built with LangGraph that analyzes any business idea using 7 specialized agents.

## Agents

| Agent | Role | Tools Used |
|---|---|---|
| Supervisor | Routes the query | - |
| Market | Market research | search_web, scrape_website |
| Finance | Financial analysis | calculate, search_web, create_chart |
| Marketing | Marketing strategy | search_web |
| Legal | Legal compliance (India) | search_web |
| Risk | Risk analysis | search_web, calculate |
| Strategy | Business roadmap | search_web |
| Report | Final report | save_report, save_pdf |

## Setup

```bash
pip install langgraph langchain langchain-openai python-dotenv openai matplotlib reportlab
```

Create a `.env` file:
```
OPENAI_API_KEY="your-api-key-here"
```

## Run

```bash
cd backend
python app.py
```

## Output
- Terminal: Full pipeline with tool call logs
- `business_report.txt` — Text report
- `business_report.pdf` — PDF report
- `*.png` — Revenue projection chart

## Architecture

```
User Query → Supervisor → Market → Finance → Marketing → Legal → Risk → Strategy → Report
                                    ↕            ↕
                                  Tools       Tools
                              (LLM decides   (Way 2 Tool
                               when to call)  Calling)
```
