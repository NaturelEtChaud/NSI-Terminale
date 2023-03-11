def rendu_monnaie_glouton(pieces, s) :
    """
    Entrées :
        pieces est un tableau d'entiers ordonnées (décroissant)
        s est la somme à rendre
    Sortie :
        M est le tableau des multiplicités pour chaque pièce, dans le même ordre
    """
    #création du tableau des mutliplicités
    M = [0]*len(pieces)
    reste = s
    i = len(pieces)-1
    while reste > 0 and i >= 0 :
        if reste - pieces[i] >= 0:
            #on peut rendre la pièce i
            reste = reste - pieces[i]
            M[i] = M[i] + 1
        else :
            i = i - 1
    return M

P = [1,2,5,10]
somme = 58
rendu = rendu_monnaie_glouton(P,somme)
print(rendu)
#vérification
calcul = 0
for i in range(len(P)):
    calcul = calcul + P[i]*rendu[i]
print(somme==calcul)