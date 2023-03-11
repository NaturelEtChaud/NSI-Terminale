##############################
# Version dynamique (on obtient juste le nombre de pièces)
##############################
def rendu_monnaie_dynamique (pieces,s) :
    """
    Entrées :

    pieces est un tableau d’entiers ordonn ées (croissant )
    nbr est le tableau contenant le nombre de pièces à rendre pour chaque nombre infé rieur ou égal s
    """

    nbr = [0]*( s+1)
    for n in range (1,s+1):
        # pire cas nbr = 1 + 1 + 1 + ... + 1
        nbr[n] = n
        for p in pieces :
            if p <= n :
                nbr[n] = min(nbr[n], 1+nbr[n-p])
    return nbr[s]

P = [1,2,5,10]
rendu = rendu_monnaie_dynamique(P,6)
print(rendu)