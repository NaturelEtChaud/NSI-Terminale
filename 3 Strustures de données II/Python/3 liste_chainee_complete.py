class Cellule :
    def __init__(self, tete, queue):
        self.tete = tete
        self.queue = queue
        
class Liste :
    def __init__(self):
        self.cellule = None
        
    def est_vide(self):
        """renvoie vraie si la liste est vide"""
        return self.cellule is None
    
    def ajoute_tete(self, valeur):
        """ajoute un élément à la liste"""
        self.cellule = Cellule(valeur, self.cellule)
    
    def renvoie_tete(self):
        """supprime et renvoie la tête de la liste si elle n'est pas vide"""
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
        """renvoie une autre liste contenant tous les éléments de la liste
        dans l'odre inverse"""
        l = self.cellule
        ord_inverse = Liste()
        while l is not None :
            ord_inverse.ajoute_tete(l.tete)
            l = l.queue
        return ord_inverse
    
    def inserer(self, valeur, position):
        """insére dans la liste une cellule contenant la valeur à la position voulue
        cette position doit être inférieure à la taille de la liste
        """
        assert 0 <= position <= len(self), "erreur d'indexation"
        if position == 0:
            self.ajoute_tete(valeur)
        else :
            l = self.cellule
            i = 0
            # on cherche la cellule précédente
            while i < position -1 :
                l = l.queue
                i = i + 1
            nv_cellule = Cellule(valeur,l.queue)
            l.queue = nv_cellule
            
    def supprimer(self, position):
        """supprime dans la liste une cellule à la position voulue
        cette position doit être inférieure à la taille de la liste
        """
        assert 0 <= position < len(self), "erreur d'indexation"
        if position == 0:
            self.renvoie_tete()
        else :
            l = self.cellule
            i = 0
            # on cherche la cellule précédente
            while i < position -1 :
                l = l.queue
                i = i + 1
            # on garde en mémoier la cellule à supprimer
            a_supprim = l.queue
            # création du nouveau lien
            l.queue = l.queue.queue
            # déconnexion de la cellule à supprimer
            a_supprim.queue = None
            
        
        
        
        
if __name__ == "__main__" :
    ma_liste = Liste()
    
    #print("la liste est-elle vide ? ", ma_liste.est_vide())
    print("la liste a pour longueur ", len(ma_liste), "\n")
    
    ma_liste.ajoute_tete(4)
    ma_liste.ajoute_tete(1)
    ma_liste.ajoute_tete(3)
    
    print(ma_liste)
    print("la liste est-elle vide ? ", ma_liste.est_vide())
    print("la liste a pour longueur ", len(ma_liste), "\n")
    
    print("insertion du nombre 5 en 2ième position")
    ma_liste.inserer(5,2)
    print(ma_liste)
    print("la liste est-elle vide ? ", ma_liste.est_vide())
    print("la liste a pour longueur ", len(ma_liste), "\n")
    
    print("suppression du nombre en 2ième position")
    ma_liste.supprimer(2)
    print(ma_liste)
    print("la liste est-elle vide ? ", ma_liste.est_vide())
    print("la liste a pour longueur ", len(ma_liste), "\n")

    print("suppression de la tête")
    print("on supprime ", ma_liste.renvoie_tete())
    print(ma_liste)
    print("la liste a pour longueur ", len(ma_liste))
    print("suppression de la tête")
    print("on supprime ", ma_liste.renvoie_tete())
    print(ma_liste)
    print("la liste a pour longueur ", len(ma_liste))
    print("suppression de la tête")
    print("on supprime ", ma_liste.renvoie_tete())
    print(ma_liste)
    print("la liste a pour longueur ", len(ma_liste))
    print("la liste est-elle vide ? ", ma_liste.est_vide(), "\n")
    

    print("attention ça va planter !!!")
    ma_liste.renvoie_tete()
