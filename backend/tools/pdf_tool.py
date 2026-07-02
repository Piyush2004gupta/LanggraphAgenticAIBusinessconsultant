from langchain_core.tools import tool
import os

@tool
def save_pdf(text: str, filename: str = "business_report.pdf") -> str:
    """Save the business report as a PDF file."""
    try:
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.units import inch
        path = os.path.join(os.getcwd(), filename)
        doc = SimpleDocTemplate(path, pagesize=letter)
        styles = getSampleStyleSheet()
        story = [Paragraph(line, styles["Normal"]) if line.strip() else Spacer(1, 0.1*inch) for line in text.split("\n")]
        doc.build(story)
        return f"PDF saved to: {path}"
    except Exception as e:
        return f"PDF error: {e}"