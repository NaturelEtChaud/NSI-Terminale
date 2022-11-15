#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def liste_chiffres(nb):
    """
    renvoie la liste de tous les chiffres qui composent un nombre
    """
    # conversion en chaîne de caractères
    nb_str = str(nb)
    liste = [int(nb_str[i]) for i in range(len(nb_str))]
    return liste
    
table_3 = [3*i for i in range(1,100//3)]

def divisible_3(nb):
    if nb < 100 :
        if nb not in table_3 :
            return False
        else :
            return True
    else :
        somme = 0
        for chiffre in liste_chiffres(nb) :
            somme += chiffre
        print(somme)
        return divisible_3(somme)
    
if __name__ == "__main__" :
    reponse = divisible_3(861)
    print("est-ce que 861 est divisible par 3 ?", reponse)
    reponse = divisible_3(3_191)
    print("est-ce que 3_191 est divisible par 3 ?", reponse)
