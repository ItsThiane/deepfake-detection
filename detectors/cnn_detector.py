#CNN feature-based detector: Détecteur CNN basé sur modèle pré-entraîné (Xception / EfficientNet) pour Deepfake


import torch
from torchvision import transforms
import timm
from PIL import Image

# Utilisation Xception pré-entraîné

#Choix du device
device = "cuda" if torch.cuda.is_available() else "cpu"

#Chargement du modèle pré-entraine(ImageNet)
model = timm.create_model('xception', pretrained=True)
model.eval().to(device)


#Trnasormations des images
transform = transforms.Compose([
    transforms.Resize((299, 299)),      #Xception standard input size
    transforms.ToTensor(),
    transforms.Normalize([0.5,0.5,0.5], [0.5,0.5,0.5])
])

#Fonction de scoring CNN
def cnn_score(image_path):
    """
    Retourne un score de probabilité Deepfake [0-1]
    """
    img = Image.open(image_path).convert("RGB")
    img_tensor = transform(img).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(img_tensor) 
        probs = torch.softmax(outputs, dim=1) #softmax pour multi-classes
        score = probs.max().item()  # valeur entre 0 et 1
    return round(score, 2)
