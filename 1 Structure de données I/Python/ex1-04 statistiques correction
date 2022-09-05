#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

notes = [randint(0,20) for i in range (1000)]

def statistiques(tab):
    """
    Entrée :
        tab est une liste d'entiers compris entre 0 et 20
    Sortie :
        stat est un dictionnaire comprenant 3 couples clef/valeur
        la clef "mini" donne la valeur la plus faible
        la clef "moye" donne la valeur moyenne arrondi à 2 chiffres àprès la virgule
        la clef "maxi" donne la valeur la plus grande
    """
    stat = {}
    mini = tab[0]
    maxi = tab[0]
    somme = tab[0]
    for i in range(1,len(tab)) :
        somme = somme + tab[i]
        if tab[i] < mini :
            mini = tab[i]
        elif tab[i] > maxi :
            maxi = tab[i]
    moye = round(somme/len(tab),2)
    stat["mini"] = mini
    stat["moye"] = moye
    stat["maxi"] = maxi
    return stat


assert statistiques(notes)["mini"] == min(notes), "tu n'as pas trouvé la note minimale"
assert statistiques(notes)["maxi"] == max(notes), "tu n'as pas trouvé la note maximale"
assert statistiques(notes)["moye"] == round(sum(notes)/len(notes),2), "tu n'as pas trouvé la note moyenne"