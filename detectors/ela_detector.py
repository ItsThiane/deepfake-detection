#Error Level Analysis (ELA) based detector
from PIL import Image
import numpy as np
import tempfile

def ela_score(image_path):
    """
    Calcule un score de suspicion Deepfake basé sur l'analyse ELA.
    Retourne un score normalisé entre 0 et 1.
    """
    original = Image.open(image_path).convert("RGB")
    tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
    original.save(tmp_file.name, "JPEG", quality=90)
    compressed = Image.open(tmp_file.name)

    diff = np.abs(np.array(original) - np.array(compressed))
    score = np.mean(diff) / 255  # Normalisation 0-1

    return round(float(score), 2)
