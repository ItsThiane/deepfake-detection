#Fusion des détecteurs



from detectors.ela_detector import ela_score
from detectors.noise_detector import noise_score
from detectors.cnn_detector import cnn_score
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tempfile
from PIL import Image

def heatmap_ela(image_path):
    """
    Génère une heatmap ELA pour visualisation
    """
    original = Image.open(image_path).convert("RGB")
    tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
    original.save(tmp_file.name, "JPEG", quality=90)
    compressed = Image.open(tmp_file.name)
    diff = np.abs(np.array(original) - np.array(compressed))
    diff_norm = (diff / diff.max() * 255).astype(np.uint8)
    heatmap = cv2.applyColorMap(diff_norm[:,:,0], cv2.COLORMAP_JET)
    return heatmap

def analyze_media(image_path):
    """
    Analyse avec vote majoritaire
    Retourne score final et détails
    """
    scores = {
        "ELA": ela_score(image_path),
        "Noise": noise_score(image_path),
        "CNN": cnn_score(image_path)
    }

    final_score = sum(scores.values()) / len(scores)
    verdict = "Deepfake suspecté" if final_score > 0.5 else "Authentique probable"
    heatmap = heatmap_ela(image_path)

    return {
        "score": round(final_score, 2),
        "details": scores,
        "verdict": verdict,
        "heatmap": heatmap
    }
