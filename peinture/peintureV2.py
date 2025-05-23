from PIL import Image
import numpy as np

def txt_vers_str(chemin_fichier):
    """Lit un fichier texte et retourne son contenu sous forme de chaîne (str)."""
    with open(chemin_fichier, "r", encoding="utf-8") as fichier:
        contenu = fichier.read()
    return contenu

# Chargement des données
donnees = txt_vers_str("peinture3.txt")

# Tailles d'image à tester (formats courants)
formats = {
    "1x1_512": (512, 512),
    "1x1_1024": (1024, 1024),
    "4x3_800x600": (800, 600),
    "4x3_1024x768": (1024, 768),
    "3x2_900x600": (900, 600),
    "3x2_1200x800": (1200, 800),
    "16x9_1280x720": (1280, 720),
    "16x9_1920x1080": (1920, 1080),
    "5x4_1280x1024": (1280, 1024),
    "21x9_2560x1080": (2560, 1080),
}

# Générer une image pour chaque format
for nom, (largeur, hauteur) in formats.items():
    image = Image.new('L', (largeur, hauteur))
    index = 0
    total_pixels = largeur * hauteur

    try:
        for y in range(hauteur):
            for x in range(largeur):
                triplet = donnees[index:index+3]
                gris = int(triplet)
                image.putpixel((x, y), gris)
                index += 3
        image.save(f"image_{nom}.png")
        print(f"[OK] image_{nom}.png générée")
    except Exception as e:
        print(f"[ERREUR] {nom} : {e}")
