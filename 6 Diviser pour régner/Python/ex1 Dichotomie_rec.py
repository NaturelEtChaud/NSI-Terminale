def dichotomie(tab, nb) :
    """
    tab est un tableau trié par ordre croissant
    recherche par récursivité si le nombre appartient au tableau tab et renvoie son indice
    dans ce programme le nb est bien présent dans le tableau
    """
    milieu = len(tab)//2
    if nb == tab[milieu]:
        return milieu
    elif nb < tab[milieu] :
        tab_gauche = [tab[i] for i in range(milieu)] #milieu exclu
        return dichotomie(tab_gauche,nb)
    else :
        tab_droite = [tab[i] for i in range(milieu+1, len(tab))] #milieu exclu
        return milieu + 1 + dichotomie(tab_droite,nb)
