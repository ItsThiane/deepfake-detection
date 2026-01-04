#noise / texture analysis: Analyse du bruit pour détecter anomalies dans l'image/vidéo
import cv2
import numpy as np

def noise_score(image_path):
    """
    Calcule un score basé sur le bruit (anomalies souvent liées aux deepfakes)
    """
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    noise = cv2.Laplacian(img, cv2.CV_64F)
    score = np.std(noise) / 100  # normalisation simple
    return min(round(score, 2), 1.0)
