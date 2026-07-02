from langchain_core.tools import tool
import urllib.request, urllib.parse, json

@tool
def search_web(query: str) -> str:
    """Search the web for business information, market data, and trends."""
    try:
        url = f"https://api.duckduckgo.com/?q={urllib.parse.quote(query)}&format=json&no_html=1"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = json.loads(urllib.request.urlopen(req, timeout=10).read())
        topics = [t["Text"] for t in data.get("RelatedTopics", []) if isinstance(t, dict) and t.get("Text")]
        return data.get("AbstractText") or "\n".join(topics[:5]) or f"No results for: {query}"
    except Exception:
        return f"Search done for: {query}. Use your knowledge to answer."