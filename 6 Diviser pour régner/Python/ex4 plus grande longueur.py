#####################################################
# méthode classique
#####################################################

def longueur(tab):
    n = len(tab)
    smax = tab[0]
    igauche = idroit = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s = s + tab[j]
            if s > smax:
                smax = s
                igauche = i
                idroit = j
    return smax, igauche, idroit


#####################################################
# méthode diviser pour régner
#####################################################

def a_cheval(T,med):
    smax = T[med]
    igauche, idroit = med, med
    #on rajoute des éléments à gauche
    i = med
    while i>0 :
        if T[i-1]>0 :
            i = i - 1
            smax = smax + T[i]
        else :
            igauche = i
            i = 0
    #on rajoute des éléments à droite
    i = med
    while i<len(T)-1 :
        if T[i+1]>0 :
            i = i + 1
            smax = smax + T[i]
        else :
            idroit = i
            i = len(T)
    return smax, igauche, idroit

def longueur2(T):
    if len(T) == 1:
        smax, igauche, idroit = T[0], 0, 0
    else :
        med = len(T)//2
        smax1, igauche1, idroit1 = longueur2(T[:med])
        smax2, igauche2, idroit2 = longueur2(T[med:])
        smax3, igauche3, idroit3 = a_cheval(T,med)
        #print(smax1, igauche1, idroit1)
        #print(smax2, igauche2, idroit2)
        #print(smax3, igauche3, idroit3)
        #print('###########')
        smax = max(smax1,smax2,smax3)
        print(med,T,smax1,smax2,smax3,smax)
        if smax == smax1 :
            smax, igauche, idroit = smax1, igauche1, idroit1
        elif smax == smax2 :
            smax, igauche, idroit = smax2, igauche2, idroit2
        else :
            smax, igauche, idroit = smax3, igauche3, idroit3
    return smax, igauche, idroit



T = [-2, -5, 6, -2, -3, 1, 5, -6]
print(longueur(T))
print(longueur2(T))
