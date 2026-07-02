from langchain_core.tools import tool
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

@tool
def create_chart(data: str, chart_type: str = "bar", title: str = "Chart") -> str:
    """Create a chart. data format: 'label1:value1,label2:value2'. chart_type: bar/pie/line"""
    try:
        pairs = [p.split(":") for p in data.split(",") if ":" in p]
        labels, values = zip(*[(p[0].strip(), float(p[1].strip())) for p in pairs])
        fig, ax = plt.subplots(figsize=(9, 5))
        if chart_type == "pie": ax.pie(values, labels=labels, autopct="%1.1f%%")
        elif chart_type == "line": ax.plot(labels, values, marker="o")
        else: ax.bar(labels, values, color=["#4CAF50","#2196F3","#FF9800","#E91E63","#9C27B0"])
        ax.set_title(title, fontweight="bold")
        path = os.path.join(os.getcwd(), f"{title.replace(' ','_').lower()}.png")
        plt.tight_layout(); plt.savefig(path, dpi=150); plt.close()
        return f"Chart saved: {path}"
    except Exception as e:
        return f"Chart error: {e}"