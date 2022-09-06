#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def nb_occurence(tab, cible):
    """
    Entrées :
        tab est un tableau d'entiers
        cible est la valeur recherchée
    Sortie :
        nb est le nombre d'occurences de la cible dans le tableau
    """
    nb = 0
    for i in range(len(tab)):
        if tab[i] == cible :
            nb = nb + 1
    return nb

T = [15, 12, 7, 6, 5, 6, -4, 3, 15, 12, 6]
assert nb_occurence(T, 2) == 0, "tu n'as pas trouvé le bon nombre d'occurences"
assert nb_occurence(T, 6) == 3, "tu n'as pas trouvé le bon nombre d'occurences"