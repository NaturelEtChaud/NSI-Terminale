# -*- coding: utf-8 -*-

from TAD import Pile

texte = "voici un texte !"

def inverse(chaine):
    pile = Pile()
    # on empile les caractères
    for i in range(len(chaine)):
        pile.empiler(chaine[i])
    # on dépile et donc on a modifié l'ordre
    reponse = ''
    while not pile.est_vide() :
        reponse = reponse + pile.depiler()
    return reponse

print(inverse(texte))