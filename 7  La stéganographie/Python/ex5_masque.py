# -*- coding: utf-8 -*-
"""
@author: Laurent Chaudet
"""

def masque(nb,bt) :
    '''
    Entrées :
        nb est un nombre entier entre 0 et 255
        bt est un nombre enter entre 0 et 8
    Sortie : un nb entier
    Rôle : on supprime les bt bits de poids faible à l'aide d'un masque
    '''

    mask = 0
    for i in range(bt,8):
        mask = mask + 2**i
    return nb & mask
    