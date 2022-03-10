##########################################################
# Fusion de deux tableaux
##########################################################

def fusion(tg, td) :
    """
    Fusionne deux listes triées en seule liste triée
    """
    resultat = [None]*(len(tg)+len(td))
    idg = 0 #sur le tableau tg
    idd = 0 #sur le tableau td

    while idg < len(tg) and idd < len(td):
        if tg[idg] < td[idd]:
            resultat[idg+idd] = tg[idg]
            idg = idg +1
        else :
            resultat[idg+idd] = td[idd]
            idd = idd +1
        if idg == len(tg):
            #le tableau tg a été complètement transféré
            while idd != len(td):
                resultat[idg+idd] = td[idd]
                idd = idd + 1
        if idd == len(td):
            #le tableau td a été complètement transféré
            while idg != len(tg):
                resultat[idg+idd] = tg[idg]
                idg = idg + 1
    return resultat


##########################################################
# Tri Fusion
##########################################################

def tri_fusion(tab) :
    """
    Sépare la liste en deux
    Et appelle récursivement sur les sous-listes la fusion/combinaison des
    résultats
    """
    if len(tab) <= 1 :
        return tab
    else :
        milieu = len(tab)//2
        tg = [tab[i] for i in range(milieu)]
        td = [tab[i] for i in range(milieu, len(tab))]
    return fusion(tri_fusion(tg), tri_fusion(td))
