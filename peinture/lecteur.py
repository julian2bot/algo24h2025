from PIL import Image
def trouver(rouge):
    return rouge%2

image_hall=Image.open("peinture/image_16x9_1920x1080.png")

#crer une matrice des pixels pour image hall
matrice=[]
for y in range(image_hall.size[1]):
    ligne=[]
    for x in range(image_hall.size[0]):
        pixel=image_hall.getpixel((x,y))

        bits = format(pixel, '08b')


        if str(bits)[6] =='0':
            nouvelle_couleur=0
        else:
            nouvelle_couleur=255
        ligne.append(nouvelle_couleur)
    matrice.append(ligne)

sortie=image_hall.copy()
for j in range(len(matrice)):
    for z in range(len(matrice[0])):
        sortie.putpixel((z,j),matrice[j][z])
sortie.save("peinture/imageout.png")