##############################
# Version dynamique (on obtient juste le nombre de pièces)
##############################
def rendu_monnaie_dynamique(pieces, s) :
    """
    Entrées :
        pieces est un tableau d'entiers ordonnées (croissant)
        nbr est le tableau contenant le nombre de pièces à rendre pour chaque nombre inférieur ou égal s
        sol est la solution
    """
    nbr = [0]*(s+1)
    sol = [[]]*(s+1)
    for n in range(1,s+1):
        #pire cas nbr = 1 + 1 + 1 + ... + 1
        nbr[n] = n
        sol[n] = [1]*n
        for p in pieces :
            if p <= n and 1 + nbr[n-p] < nbr[n] :
                nbr[n] = 1 + nbr[n-p]
                sol[n] = sol[n-p].copy()
                sol[n].append(p)
                print(sol)
    return sol[s]

P = [1,2,5,10]
rendu = rendu_monnaie_dynamique(P,6)
print(rendu)
