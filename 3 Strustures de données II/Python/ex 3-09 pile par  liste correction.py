from TAD import Cellule

class Pile :
    def __init__(self):
        self.data = None
        
    def est_vide(self):
        return self.data is None
    
    def empiler(self, valeur):
        self.data = Cellule(valeur, self.data)
    
    def depiler(self):
        assert self.data is not None, "Pile Vide !"
        valeur = self.data.tete
        self.data = self.data.queue
        return valeur
    
    def sommet(self):
        assert self.data is not None, "Pile Vide !"
        return self.data.tete
    
    def __str__(self):
        """dans cette version simple, on espère que les élèments s'écrivent 
        avec uniquement uniquement un caractère
        """
        if self.data is None:
            affichage = "| |\n"
        else :
            affichage = ""
            l = self.data
            while l is not None :
                affichage = affichage + "|"+str(l.tete)+"|\n"
                l = l.queue
        affichage = affichage + "***"
        return affichage
    
    def __len__(self):
        n = 0
        l = self.data
        while l is not None :
            l = l.queue
            n = n + 1
        return n
        
        
if __name__ == "__main__" :
    ma_pile = Pile()
    
    print(ma_pile)
    print("la pile est-elle vide ?", ma_pile.est_vide())
    print("la pile a pour longueur ", len(ma_pile), "\n")
    
    ma_pile.empiler(1)
    print(ma_pile)
    print("la pile est-elle vide ?", ma_pile.est_vide())
    print("la pile a pour longueur ", len(ma_pile), "\n")
    
    ma_pile.empiler(2)
    print("on empile 2")
    print(ma_pile)
    ma_pile.depiler()
    print("on dépile")
    print(ma_pile)
    print("le sommet est ", ma_pile.sommet(), "\n")
    
    print("on empile 3 puis 4 puis 5")
    ma_pile.empiler(3)
    ma_pile.empiler(4)
    ma_pile.empiler(5)
    print(ma_pile)
    print("la pile est-elle vide ?", ma_pile.est_vide())
    print("la pile a pour longueur ", len(ma_pile), "\n")
    
    print("on dépile deux fois")
    ma_pile.depiler()
    ma_pile.depiler()
    print(ma_pile)
    print("la pile est-elle vide ?", ma_pile.est_vide())
    print("la pile a pour longueur ", len(ma_pile), "\n")