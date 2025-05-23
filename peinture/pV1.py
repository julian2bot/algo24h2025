from PIL import Image
import math

def txt_vers_str(chemin_fichier):
    with open(chemin_fichier, "r", encoding="utf-8") as fichier:
        contenu = fichier.read()
    return contenu

donnees = txt_vers_str("peinture3.txt")
nb_pixels = len(donnees) // 3

# Trouver tous les couples (largeur, hauteur) possibles
tailles = []
for i in range(1, int(math.sqrt(nb_pixels)) + 1):
    if nb_pixels % i == 0:
        tailles.append((i, nb_pixels // i))
        if i != nb_pixels // i:
            tailles.append((nb_pixels // i, i))

for largeur, hauteur in tailles:
    image = Image.new('L', (largeur, hauteur))
    index = 0
    for y in range(hauteur):
        for x in range(largeur):
            triplet = donnees[index:index+3]
            try:
                gris = int(triplet)
            except Exception:
                gris = 0
            image.putpixel((x, y), gris)
            index += 3
    image.save(f"image_{largeur}x{hauteur}.png")
    print(f"Image générée : image_{largeur}x{hauteur}.png")
