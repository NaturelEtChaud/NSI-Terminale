#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

T = [randint(-100,100) for i in range(100)]

def tri_bulles(tab):
    """
    Entrée :
        tab est un tableau d'entiers
    Sortie :
        tri est un tableau trié dans l'ordre croissant contenant exactement les mêmes valeurs que tab
    """
    # on effectue une copie du tableau 
    tri = tab.copy()
    modifie = True
    while modifie :
        modifie = False
        for i in range(1,len(tri)) :
            if tri[i-1] > tri[i] :
                tri[i-1], tri[i] = tri[i], tri[i-1]
                modifie = True
    return tri
    
assert tri_bulles(T) == sorted(T), "le tableau n'est pas trié"
