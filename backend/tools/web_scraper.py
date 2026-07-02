from langchain_core.tools import tool
import urllib.request, re

@tool
def scrape_website(url: str) -> str:
    """Scrape text content from a website URL."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        html = urllib.request.urlopen(req, timeout=10).read().decode("utf-8", errors="ignore")
        html = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", html, flags=re.DOTALL)
        text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()
        return text[:2000]
    except Exception as e:
        return f"Could not scrape {url}: {e}"
