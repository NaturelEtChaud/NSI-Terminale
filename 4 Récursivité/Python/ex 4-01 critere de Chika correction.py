#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def chika_v1(nb):
    if nb < 7 :
        return False
    elif nb == 7 :
        return True
    else :
        unite = nb % 10
        dizaine = nb // 10
        print(dizaine + 5*unite) # ligne non obligatoire
        return chika_v1(dizaine + 5*unite)
    

table_7 = [7*i for i in range(1,100//7)]

def chika_v2(nb):
    if nb < 100 :
        if nb not in table_7 :
            return False
        else :
            return True
    else :
        unite = nb % 10
        dizaine = nb // 10
        print(dizaine + 5*unite) # ligne non obligatoire
        return chika_v2(dizaine + 5*unite)
    
if __name__ == "__main__" :
    reponse = chika_v1(861)
    print("est-ce que 861 est divisible par 7 ?", reponse)
    reponse = chika_v2(861)
    print("est-ce que 861 est divisible par 7 ?", reponse)
    reponse = chika_v1(3_191)
    print("est-ce que 3_191 est divisible par 7 ?", reponse)
    reponse = chika_v2(3_191)
    print("est-ce que 3_191 est divisible par 7 ?", reponse)
