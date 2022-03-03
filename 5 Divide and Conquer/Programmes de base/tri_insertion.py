# -*- coding: utf-8 -*-

import random as rd

#taille du tableau
n=10

T=[rd.randint (0 ,100) for i in range(n)]
print(T)

for i in range(1,n) :
    #on prend un nouvel indice
    j = i
    while (j > 0) and (T[j-1] > T[j]) :
        #tant qu'à gauche, il y a un élément plus grand
        #on les échange
        T[j], T[j-1] = T[j-1], T[j]
        j = j - 1
        print(T)
