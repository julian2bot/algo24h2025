def txt_vers_str(chemin_fichier):
    """Lit un fichier texte et retourne son contenu sous forme de chaîne (str)."""
    with open(chemin_fichier, "r", encoding="utf-8") as fichier:
        contenu = fichier.read()
    return contenu

donnees = txt_vers_str("peinture3.txt")

leng = 6912000
largeur = 1518 
hauteur = 1518

from PIL import Image
import numpy as np

image = Image.new('L', (largeur, hauteur))

# pixels = [(int(c) / 9.0 * 255) for c in donnees]

# # for x in range(largeur):
# #     for y in range(hauteur):
# #         niveau_gris = str(texte[x])  # La valeur va de 0 (noir) à 255 (blanc)
# #         image.putpixel((x, y), niveau_gris)

# image = Image.new('L', (largeur, hauteur))
# image.putdata([int(p) for p in pixels])
# image.save("image_str_gris.png")


index = 0
for y in range(hauteur):
    for x in range(largeur):
        try:
            triplet = donnees[index:index+3]
            # print(triplet)
            gris = int(triplet)  
            image.putpixel((x, y), gris)
            index += 3
        except Exception:
            print("aie + ", triplet) 
       

        
image.save("image_str_gris.png")