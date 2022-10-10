from TAD import File

def look_n_say(graine, n):
    '''
    Entrées :
        graine est une file non vide contenant uniquement des chiffres
        n est le nombre d'itérations attendu
    Sortie :
        lns est une file résultat du processus look'n'say après n itérations
    ATTENTION
        il faut lire le résultat de la droite vers la gauche
    '''
    assert not graine.est_vide(), "la graine ne doit pas être une file vide"
    
    serie = graine.copie()
    for i in range(n):
        lns = File()
        while not serie.est_vide() :
            chiffre = serie.defiler()
            nb = 1 # pour compter le nombre de répétitions du chiffre
            while not serie.est_vide() and serie.tete() == chiffre :
                serie.defiler()
                nb = nb + 1
            lns.enfiler(nb)
            lns.enfiler(chiffre)
        print(lns)  # cette ligne peut être supprimer
        serie = lns.copie()
    return lns
    
    
    
        
        
if __name__ == "__main__" :
    graine = File()
    graine.enfiler(1)
    print("la graine est ", graine)
    
    n = 10
    lns = look_n_say(graine,n)
    print("après",n,"itérations la suite Look'n'Say donne")
    print(lns)