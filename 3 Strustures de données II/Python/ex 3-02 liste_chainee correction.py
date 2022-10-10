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
    
    def __str__(self):
        """affichage des éléments de la liste dans l'ordre"""
        affichage = "["
        l = self.cellule
        if l is not None :
            affichage = affichage + str(l.tete)
            l = l.queue 
        while l is not None :
            affichage = affichage + "," + str(l.tete)
            l = l.queue
        affichage = affichage + "]"
        return affichage
    
    def __len__(self):
        """donne la longueur de la liste"""
        n = 0
        l = self.cellule
        while l is not None :
            n = n + 1
            l = l.queue
        return n
    
    def __getitem__(self, n):
        """donne le n-ième élément de la liste"""
        assert 0 <= n <len(self), "erreur d'indexation"
        i = 0
        l = self.cellule
        while i < n :
            i = i + 1
            l = l.queue
        return l.tete
    
    def renverser(self):
        """renvoie une autre liste contenant tous les éléments de self
        dans l'odre inverse"""
        l = self.cellule
        ord_inverse = Liste()
        while l is not None :
            ord_inverse.ajouter_tete(l.tete)
            l = l.queue
        return ord_inverse
        
        
        
if __name__ == "__main__" :
    ma_liste = Liste()
    
    print(ma_liste)
    print("la liste est-elle vide ? ", ma_liste.est_vide())  
    print("la liste a pour longueur ", len(ma_liste), "\n")
    
    ma_liste.ajouter_tete(4)
    print(ma_liste)
    print("la liste est-elle vide ? ", ma_liste.est_vide())
    print("la liste a pour longueur ", len(ma_liste), "\n")
    ma_liste.ajouter_tete(1)
    ma_liste.ajouter_tete(3)
    print(ma_liste)
    print("la liste a pour longueur ", len(ma_liste))
    print("le deuxième élément de la liste est ", ma_liste[1], "\n")
    
    liste2 = ma_liste.renverser()
    print("la liste dans l'ordre inverse ", liste2)
