##############################
# Version récursive (on obtient juste le nombre de pièces)
##############################
def rendu_monnaie_recursif(pieces, s) :
    """
    Entrées :
        pieces est un tableau d'entiers ordonnées (croissant)
        nbr est le nombre de pièces à rendre
    """
    if s == 0:
        return 0
    else :
        #pire cas s = 1 + 1 + 1 + ... + 1
        nbr = s
        for p in pieces :
            if p <= s :
                nbr = min(nbr, 1+rendu_monnaie_recursif(pieces, s-p))
        return nbr

P = [1,2,5,10]
rendu = rendu_monnaie_recursif(P,4)
print(rendu)