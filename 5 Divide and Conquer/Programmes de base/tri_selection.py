# -*- coding: utf-8 -*-

import random as rd

#taille du tableau
n=10

T=[rd.randint (0 ,100) for i in range(n)]
print(T)

for i in range(0,n) :
    indice_min = i
    #on cherche le minimum à partir de T[i]
    for j in range(i+1,n) :
        if T[indice_min] > T[j] :
            indice_min = j
    #on les échange
    T[indice_min], T[i] = T[i], T[indice_min]
    print(T)
