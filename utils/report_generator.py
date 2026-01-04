# Générateur de rapport PDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import os
import cv2

REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)

def generate_pdf_report(result, filename="report"):
    """
    Fonction pour generater le rapport PDF
    
    :param result
    :param filename
    """
    path = os.path.join(REPORT_DIR, f"{filename}_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf")
    c = canvas.Canvas(path, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, "Deepfake Detection Report")
    c.setFont("Helvetica", 12)
    c.drawString(50, 720, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(50, 700, f"Verdict: {result['verdict']}")
    c.drawString(50, 680, f"Score global: {result['score']}")
    c.drawString(50, 660, "Détails détecteurs:")
    y = 640
    for k, v in result["details"].items():
        c.drawString(70, y, f"{k}: {v}")
        y -= 20
    # Ajout heatmap si disponible
    heatmap = result.get("heatmap", None)
    if heatmap is not None:
        heatmap_path = os.path.join(REPORT_DIR, "temp_heatmap.jpg")
        cv2.imwrite(heatmap_path, heatmap)
        c.drawImage(heatmap_path, 50, y-200, width=500, height=200)
    c.save()
    return path












