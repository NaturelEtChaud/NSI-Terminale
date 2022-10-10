class Cellule :
    def __init__(self, tete, queue):
        self.tete = tete
        self.queue = queue
        
        
if __name__ == "__main__" :
    ma_liste = Cellule(3, Cellule(1, Cellule(4, None)))
    
    # le premier élément de la liste
    premier = ma_liste.tete
    print(premier)
    
    # le deuxième élément de la liste
    deuxieme = ma_liste.queue.tete
    print(deuxieme)
    
    # le troisième élément de la liste
    troisieme = ma_liste.queue.queue.tete
    print(troisieme)