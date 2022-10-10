class Cellule :
    def __init__(self, tete, queue):
        self.tete = tete
        self.queue = queue
        
class Liste :
    def __init__(self):
        self.cellule = None
        
    def est_vide(self):
        return self.cellule is None
    
    def ajouter_tete(self, valeur):
        self.cellule = Cellule(valeur, self.cellule)
    
    def renvoyer_tete(self):
        assert self.cellule is not None, "Liste Vide !"
        tete = self.cellule.tete
        if self.cellule.queue is not None :
            self.cellule = Cellule(self.cellule.queue.tete, self.cellule.queue.queue)
        else :
            self.cellule = None
        return tete
        
        
        
if __name__ == "__main__" :
    ma_liste = Liste()
    
    # la liste est-elle vide ?
    print("la liste est-elle vide ?", ma_liste.est_vide(), "\n")
    
    ma_liste.ajouter_tete(4)
    print("la tête est ", ma_liste.cellule.tete)
    ma_liste.ajouter_tete(1)
    print("la tête est ", ma_liste.cellule.tete)
    ma_liste.ajouter_tete(3)
    print("la tête est ", ma_liste.cellule.tete)
    
    # la liste est-elle vide ?
    print("la liste est-elle vide ?", ma_liste.est_vide(), "\n")

    a = ma_liste.renvoyer_tete()
    print("on supprime ", a)
    b = ma_liste.renvoyer_tete()
    print("on supprime ", b)
    c = ma_liste.renvoyer_tete()
    print("on supprime ", c)
    
    # la liste est-elle vide ?
    print("la liste est-elle vide ?", ma_liste.est_vide(), "\n")
    
    # attention ça va planter !!!!
    d = ma_liste.renvoyer_tete()
