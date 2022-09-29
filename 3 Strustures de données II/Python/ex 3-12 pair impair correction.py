from TAD import File

def parite(file):
    """
    Entrée :
        file est une File ne contenant que des nombres entiers
    Rôle :
        faire le tri entre les nombres pairs et impairs de file
    Sortie :
        pairs est une File contenant tous les nombres pairs de file
        impairs est une File contenant tous les nombres impairs de la file
    """
    pairs = File()
    impairs = File()
    while not file.est_vide() :
        nombre = file.defiler()
        if nombre%2 == 0 :
            pairs.enfiler(nombre)
        else :
            impairs.enfiler(nombre)
    return pairs, impairs

if __name__ == "__main__" :
    from random import randint
    
    # création d'une file contenant 15 nombres entiers pris au hasard entre -100 et 100
    file = File() 
    for i in range(15):
        file.enfiler(randint(-100,100))
    print("la file de 15 entiers est ", file, "\n")
    
    # séparation des pairs et des impaires
    p, i = parite(file)
    print("les nombres pairs sont ", p)
    print("les nombres impairs sont ", i)