from TAD import Liste

class Dico:
    def __init__(self):
        self.liste = Liste()
    
    def est_vide(self):
        """renvoie vraie si le dictionnaire est vide"""
        return self.liste.est_vide()
    
    def ajouter(self, cle, valeur):
        """ajoute un couple cle/valeur dans le dictionnaire"""
        assert not self.cles().appartient(cle) ,"cette clé a déjà été utilisée"
        self.liste.ajoute_tete((cle, valeur))
        
    def supprimer(self, ma_cle):
        """supprime le couple clé/valeur ayant pour clé ma_cle"""
        n = len(self.liste)
        i = 0
        trouve = False
        while i<n and not trouve:
            cle, valeur = self.liste[i]
            if cle == ma_cle :
                trouve = True
            else :
                i = i + 1
        if trouve :
            self.liste.supprimer(i)
        
    
    def valeur(self, ma_cle):
        """"renvoie la valeur du couple clé/valeur
        ATTENTION renvoie -1 si la clé donnée ne correspond à aucune clé du dictionnaire"""
        reponse = -1
        n = len(self.liste)
        i = 0
        while i<n :
            cle, valeur = self.liste[i]
            if cle == ma_cle :
                reponse = valeur
                i = n
            i = i + 1
        return reponse
        
    
    def cles(self):
        """donne la liste de toutes les clés"""
        n = len(self.liste)
        les_cles = Liste()
        for i in range(n):
            cle, valeur = self.liste[i]
            les_cles.ajoute_tete(cle)
        return les_cles
        

    
    
    
        
        
if __name__ == "__main__" :
    mon_dico = Dico()
    
    print("mon dictionnaire est-il vide ?", mon_dico.est_vide(), "\n")
    
    print("on ajoute le couple clé/valeur ('Hedy':'Lamarr')")
    mon_dico.ajouter('Hedy', 'Lamarr')
    print("on ajoute le couple clé/valeur ('John':'Conway')")
    mon_dico.ajouter('John', 'Conway')
    print("on ajoute le couple clé/valeur ('Ada':'Lovelace')")
    mon_dico.ajouter('Ada', 'Lovelace')
    print("mon dictionnaire est-il vide ?", mon_dico.est_vide(), "\n")
    
    print("la liste des clés est ", mon_dico.cles(), "\n")
    
    print("quel est le nom de John ?", mon_dico.valeur("John"), "\n")
    
    print("quel est le nom de Jean ?", mon_dico.valeur("Jean"), "\n")
    
    mon_dico.supprimer("John")
    print("on supprime le couple de clé 'John'.")
    print("la liste des clés est ", mon_dico.cles(), "\n")
    
    print("ATTENTION ça va planter")
    print("on ajoute le couple clé/valeur ('Hedy':'Lamer')")
    mon_dico.ajouter('Hedy', 'Lamer')