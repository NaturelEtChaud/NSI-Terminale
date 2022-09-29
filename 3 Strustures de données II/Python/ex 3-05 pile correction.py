class Pile :
    def __init__(self):
        self.data = []
        
    def est_vide(self):
        return self.data == []
    
    def empiler(self, valeur):
        self.data.append(valeur)
    
    def depiler(self):
        assert self.data != [], "Pile Vide !"
        return self.data.pop()
    
    def sommet(self):
        assert self.data != [], "Pile Vide !"
        return self.data[-1]
    
    def __str__(self):
        """dans cette version simple, on espère que les élèments s'écrivent 
        avec uniquement uniquement un caractère
        Une version améliorée dans le corrigé de l'exercice 3-06
        """
        if self.data == []:
            affichage = "| |\n"
        else :
            affichage = ""
            for i in range(len(self.data)):
                affichage = affichage + "|"+str(self.data[-i-1])+"|\n"
        affichage = affichage + "***"
        return affichage
    
    def __len__(self):
        return len(self.data)
        
        
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