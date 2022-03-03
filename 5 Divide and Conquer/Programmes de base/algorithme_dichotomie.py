# -*- coding: utf-8 -*-

T = [1, 5, 24, 28, 29, 31, 33, 34, 52]

def recherche_dicho(T,v):
    '''
    T est un tableau trié par ordre croissant
    v est la valeur recherchée
    '''
    n = len(T)
    
    mini = 0
    med = 0
    maxi = n-1
    while mini < maxi:
        med = (mini + maxi)//2
        if T[med]< v :
            #v est dans la partie supérieure du tableau
            mini = med +1
        elif T[med] > v :
            #v est dans la partie inférieure du tableau
            maxi = med -1
        else :
            maxi = med
            mini = med
    if T[mini]==v :
        indice = mini
    else:
        indice = -1

    return indice