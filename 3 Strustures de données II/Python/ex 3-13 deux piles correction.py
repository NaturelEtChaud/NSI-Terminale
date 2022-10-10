from TAD import Pile

class File :
    def __init__(self):
        self.entree = Pile()
        self.sortie = Pile()
        
    def est_vide(self):
        return self.entree.est_vide() and self.sortie.est_vide()
    
    def enfiler(self, valeur):
        self.entree.empiler(valeur)
    
    def defiler(self):
        assert not self.entree.est_vide() or not self.sortie.est_vide(), "file Vide !"
        if self.sortie.est_vide() :
            # on dépile entree dans sortie
            while not self.entree.est_vide() :
                self.sortie.empiler(self.entree.depiler())
        return self.sortie.depiler()
        
    def tete(self):
        assert not self.entree.est_vide() or not self.sortie.est_vide(), "file Vide !"
        if self.sortie.est_vide() :
            # on dépile entree dans sortie
            while not self.entree.est_vide() :
                self.sortie.empiler(self.entree.depiler())
        return self.sortie.sommet()
    
    def __str__(self):
        if self.est_vide():
            affichage = ">>"
        else :
            # on fait une copie des deux piles pour les dépiler sans risques
            entree_temp = self.entree.copie()
            sortie_temp = self.sortie.copie()
            affichage = '>'
            # on dépile la copie de la pile sortie
            # les éléments sont dans le bon ordre
            while not sortie_temp.est_vide() :
                valeur = sortie_temp.depiler()
                affichage = str(valeur) + '_' + affichage
            # on rempile la pile entree dans la pile sortie
            # car les valeurs ne sont pas dans le bon ordre
            while not entree_temp.est_vide() :
                sortie_temp.empiler(entree_temp.depiler())
            # on reprend la suite de l'affichage
            while not sortie_temp.est_vide() :
                valeur = sortie_temp.depiler()
                affichage = str(valeur) + '_' + affichage
            affichage = '>_' + affichage
        return affichage
    
    def __len__(self):
        return len(self.entree) + len(self.sortie)
    
    #def renverser(self):
    #    self.data = [self.data[-i-1] for i in range(len(self.data))]
        
        
if __name__ == "__main__" :
    ma_file = File()
    
    print(ma_file)
    print("la file est-elle vide ?", ma_file.est_vide())
    print("la file a pour longueur ", len(ma_file), "\n")
    
    ma_file.enfiler(1)
    print("on enfile 1")
    print(ma_file)
    print("la file est-elle vide ?", ma_file.est_vide())
    print("la file a pour longueur ", len(ma_file), "\n")
    
    ma_file.enfiler(2)
    print("on enfile 2")
    print(ma_file)
    ma_file.defiler()
    print("on défile")
    print(ma_file, "\n")
    
    print("on enfile 3 puis 4 puis 5")
    ma_file.enfiler(3)
    ma_file.enfiler(4)
    ma_file.enfiler(5)
    print(ma_file)
    print("la file est-elle vide ?", ma_file.est_vide())
    print("la file a pour longueur ", len(ma_file))
    print("le premier élément de la file est ", ma_file.tete(), "\n")
       
    print("on défile deux fois")
    ma_file.defiler()
    ma_file.defiler()
    print(ma_file)
    print("la file est-elle vide ?", ma_file.est_vide())
    print("la file a pour longueur ", len(ma_file), "\n")