# -*- coding: utf-8 -*-

texte = "voici un texte"

def inverse(chaine):
    long = len(chaine)
    if long == 0:
        return chaine
    elif long == 1:
        return chaine
    else:
        #on prend le premier caractère
        car = chaine[0]
        #on le place à fin de la chaine sans le premier caractère
        return inverse(chaine[1:])+car

print(inverse(texte))