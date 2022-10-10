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
        """
        dans cette version la largeur de la pile s'adapte aux nombres de cractères
        nécessaire pour écrire tous les élments de la pile
        """
        if self.data == []:
            affichage = "| |\n***"
        else :
            affichage = ""
            largeur = max([len(str(e)) for e in self.data])
            for i in range(len(self.data)):
                nb_car = len(str(self.data[-i-1]))
                nb_space = largeur-nb_car
                affichage = affichage + "|"+' '*nb_space+str(self.data[-i-1])+"|\n"
            affichage = affichage + "*"*(largeur+2)
        return affichage
    
    def __len__(self):
        return len(self.data)
    
    def echanger(self):
        assert len(self.data) >=2, "La pile doit avoir au minimum 2 éléments"
        self.data[-2], self.data[-1] = self.data[-1], self.data[-2]
        
    def renverser(self):
        self.data = [self.data[-i-1] for i in range(len(self.data))]
        
        
if __name__ == "__main__" :
    ma_pile = Pile()
    
    print(ma_pile)
    print("la pile est-elle vide ?", ma_pile.est_vide())
    print("la pile a pour longueur ", len(ma_pile), "\n")
    
    ma_pile.empiler(1)
    print(ma_pile)
    print("la pile est-elle vide ?", ma_pile.est_vide())
    print("la pile a pour longueur ", len(ma_pile), "\n")
    
    ma_pile.empiler(12)
    print("on empile 12")
    print(ma_pile)
    ma_pile.depiler()
    print("on dépile")
    print(ma_pile)
    print("le sommet est ", ma_pile.sommet(), "\n")
    
    print("on empile 32 puis 154 puis 5")
    ma_pile.empiler(32)
    ma_pile.empiler(154)
    ma_pile.empiler(5)
    print(ma_pile)
    print("la pile est-elle vide ?", ma_pile.est_vide())
    print("la pile a pour longueur ", len(ma_pile), "\n")
    
    print("on échange les 2 éléments au sommet de la pile")
    ma_pile.echanger()
    print(ma_pile)
    print("on renverse la pile")
    ma_pile.renverser()
    print(ma_pile, "\n")
    
    print("on dépile deux fois")
    ma_pile.depiler()
    ma_pile.depiler()
    print(ma_pile)
    print("la pile est-elle vide ?", ma_pile.est_vide())
    print("la pile a pour longueur ", len(ma_pile), "\n")
    
    
    p = Pile()
    print(p)
    p.empiler(12)
    print(p)
    p.empiler(14)
    print(p)
    p.empiler(8)
    print(p)
    p.depiler()
    print(p)
    p.empiler(15)
    print(p)
    