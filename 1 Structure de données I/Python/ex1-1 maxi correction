#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

#################################
# première version
#################################

# création d'un tableau d'entiers
T = [randint(-100,100) for i in range(100)]

def maxi_v1(tab):
    """
    Entrée :
        tab est un tableau d'entiers
    Sortie :
        le tuple maxi, position
        maxi est la valeur maximale du tableau
        position est la première position de cette valeur maximale dans le tableau
    """
    position = 0
    maxi = tab[0]
    for i in range(1,len(tab)):
        if tab[i] > maxi :
            maxi = tab[i]
            position = i
    return maxi, position

assert maxi_v1(T)[0] == max(T), "tu n'as pas trouvé le maximum version 1"
assert T[maxi_v1(T)[1]] == max(T), "tu n'as pas trouvé se situe le maximum version 1"



#################################
# deuxième version les entiers sont entre 0 et 20
#################################

# création d'un tableau d'entiers entre 0 et 20
T20 = [randint(0,20) for i in range(100)]

def maxi_v2(tab):
    """
    Entrée :
        tab est un tableau d'entiers entre 0 et 20
    Sortie :
        le tuple maxi, position
        maxi est la valeur maximale du tableau
        position est la première position de cette valeur maximale dans le tableau
    """
    position = 0
    maxi = tab[0]
    i = 0
    while i < len(tab) and maxi != 20 :
        if tab[i] > maxi :
            maxi = tab[i]
            position = i
        i = i + 1
    return maxi, position

assert maxi_v2(T20)[0] == max(T20), "tu n'as pas trouvé le maximum version 2"
assert T20[maxi_v2(T20)[1]] == max(T20), "tu n'as pas trouvé se situe le maximum version 2"