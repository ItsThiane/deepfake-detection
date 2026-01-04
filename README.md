# Deepfake Detection Platform

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.27-orange)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---
### Interface principale

![Interface Streamlit](samples/interface.png)


## Description

Ce projet est un **prototype de détection de deepfakes** utilisant plusieurs détecteurs combinés :

- **ELA (Error Level Analysis)** pour détecter les retouches JPEG  
- **Analyse du bruit / Laplacian** pour repérer les anomalies subtiles  
- **CNN Xception pré-entraîné** (ImageNet) pour un score global approximatif  

**Fonctionnalités :**

- Upload **image ou vidéo**  
- Analyse frame par frame pour les vidéos  
- **Score global et verdict** ("Deepfake suspecté" ou "Authentique probable")  
- **Heatmaps** pour visualiser les zones suspectes  
- Export d’un **rapport PDF** complet  

> Ce projet est à **but éducatif et démonstratif**. Ne pas utiliser à des fins douteuses.

---

## Installation

1. Cloner le dépôt :
```bash
git clone https://github.com/<votre-utilisateur>/deepfake-detection-streamlit.git
cd deepfake-detection-streamlit

1. Installer les dépendances:
pip install -r requirements.txt

3. Lancer Streamlit:
streamlit run app.py

4. Dans l’interface, vous pouvez: 
Uploader une image ou une vidéo,
Puis Visualiser le score et verdict
Au besoin, télécharger le rapport PDF
Pour les vidéos, le système analyse jusqu’à 30 frames pour une démo rapide.
