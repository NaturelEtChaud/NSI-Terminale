#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def paire_impaire(nombres):
    """
    Entrée :
        nombres est un tuple contenant des entiers
    Sorties :
        paire est la liste des entiers paires contenu dans nombres
        impaire est la liste des entiers impaires contenu dans nombres
    """
    paire = []
    impaire = []
    for i in range(len(nombres)):
        if nombres[i]%2 == 0:
            paire.append(nombres[i])
        else :
            impaire.append(nombres[i])
    return paire, impaire

nombres = [15, 12, 7, 6, 5, 6, -4, 3, 15, 12, 6]
assert paire_impaire(nombres)[0] == [12, 6, 6, -4, 12, 6], "tu n'as pas trouvé la liste des nombres paires"
assert paire_impaire(nombres)[1] == [15, 7, 5, 3, 15], "tu n'as pas trouvé la liste des nombres impaires"