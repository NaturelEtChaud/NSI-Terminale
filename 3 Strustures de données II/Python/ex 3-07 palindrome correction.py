from TAD import Pile

def palindrome(mot):
    """
    Entrée :
        mot est une chaîne de caractères uniquement en minuscule
        sans aucun caractère spécial, ni chiffre, ni espace
    Sortie :
        un booléen, vrai si mot est un palindrome
    """
    n = len(mot)
    mediane = n//2
    # on empile la première moitié des caractères
    pile = Pile()
    for i in range(mediane):
        pile.empiler(mot[i])
    # si mot contient un nombre impair de caractères
    # on le passe le caractère unique du milieu
    if n%2 == 1 :
        i = mediane + 1
    else :
        i = mediane
    # on procède à la vérification en dépilant et en comparant aux restes
    # des caractères
    reponse = True
    while i<n and reponse == True :
        if pile.depiler() != mot[i]:
            reponse = False
        i = i + 1
    return reponse
    