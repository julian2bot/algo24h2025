def txt_vers_str(chemin_fichier):
    """Lit un fichier texte et retourne son contenu sous forme de chaîne (str)."""
    with open(chemin_fichier, "r", encoding="utf-8") as fichier:
        contenu = fichier.read()
    return contenu

mouvements = txt_vers_str("mouvement6.txt").split(",")

pos_init=[1,2,3,4,5,6,7,8,9]
drones=[1,2,3,4,5,6,7,8,9]

def rotations(drones, rotation):
    match rotation[0]:
        case "e":
            mv1 = int(rotation[1])-1
            mv2 = int(rotation[2])-1
            drones[mv2], drones[mv1] = drones[mv1], drones[mv2]
        case "r":
            pivot = int(rotation[1]) - 1
            i = 0
            while i<len(drones) and pivot-i>=0 and pivot+i<len(drones):
                drones[pivot-i], drones[pivot+i] = drones[pivot+i], drones[pivot-i]
                i+=1
            
        case "p":
            mv1 = int(rotation[1])
            mv2 = int(rotation[2])
            i1 = drones.index(mv1)
            i2 = drones.index(mv2)
            drones[i1], drones[i2] = drones[i2], drones[i1]
        case "t":
            mv1 = int(rotation[1])
            rotations(drones,"r" + str(drones.index(mv1) +1 ))

    # return drones

def les_rotations(liste_rota, drones, pos_init):
    index = 0
    while index==0 or drones != pos_init:
        for i in liste_rota:
            # print(i)
            rotations(drones,i)
            # print(drones)
        print("\n\n FIN INDEX ", str(index))
        index+=1
    print(drones)
    print(pos_init)
    return index

les_rotations(mouvements, drones, pos_init)
