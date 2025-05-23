# -*- coding: utf-8 -*-
def txt_vers_str(chemin_fichier):
    """Lit un fichier texte et retourne son contenu sous forme de chaîne (str)."""
    with open(chemin_fichier, "r", encoding="utf-8") as fichier:
        contenu = fichier.read()
    return contenu

texte= txt_vers_str("message.txt")

import re
from collections import Counter

def mots_avec_lettres_total(text, lettres, minimum_total):
    mots = re.findall(r'\b\w+\b', text.lower())
    resultat = []

    for mot in mots:
        compteur = Counter(mot)
        total = sum(compteur[lettre] for lettre in lettres)
        if total == minimum_total:
            resultat.append(mot)

    return resultat

lettres = ['i', 'j']
minimum_total = 3

print(mots_avec_lettres_total(texte, lettres, 3))