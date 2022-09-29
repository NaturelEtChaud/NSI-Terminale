from TAD import Liste

HTAILLE = 5 # taille de la table de hachage

def hachage(cle):
	code = 0
	for car in cle :
		code = code + ord(car)
	return code % HTAILLE

class Dico:
    def __init__(self):
        self.table = [None]*HTAILLE
    
    def ajouter(self, cle, valeur):
        """ajoute un couple cle/valeur dans le dictionnaire"""
        # on devrait faire une assertion pour les doublons sur les clés...
        indice = hachage(cle)
        if self.table[indice] is None :
            self.table[indice] = Liste()
        self.table[indice].ajoute_tete((cle, valeur))
        
    def valeur(self, ma_cle):
        """"renvoie la valeur du couple clé/valeur
        ATTENTION renvoie -1 si la clé donnée ne correspond à aucune clé du dictionnaire"""
        indice = hachage(ma_cle)
        reponse = -1
        n = len(self.table[indice])
        i = 0
        while i<n :
            cle, valeur = self.table[indice][i]
            if cle == ma_cle :
                reponse = valeur
                i = n
            i = i + 1
        return reponse
        
    
    def cles(self):
        """donne la liste de toutes les clés"""
        les_cles = Liste()
        for indice in range(HTAILLE):
            if self.table[indice] is not None :
                n = len(self.table[indice])
                for i in range(n):
                    cle, valeur = self.table[indice][i]
                    les_cles.ajoute_tete(cle)
        return les_cles
        

    
    
    
        
        
if __name__ == "__main__" :
    print("création du dictionnaire")
    mon_dico = Dico()
    
    print("on ajoute le couple clé/valeur ('Hedy':'Lamarr')")
    mon_dico.ajouter('Hedy', 'Lamarr')
    print("on ajoute le couple clé/valeur ('John':'Conway')")
    mon_dico.ajouter('John', 'Conway')
    print("on ajoute le couple clé/valeur ('Ada':'Lovelace')")
    mon_dico.ajouter('Ada', 'Lovelace')
    
    print("la liste des clés est ", mon_dico.cles(), "\n")
    
    print("quel est le nom de John ?", mon_dico.valeur("John"), "\n")
    print("quel est le nom de John ?", mon_dico.valeur("Hedy"), "\n")
    
    print("quel est le nom de Jean ?", mon_dico.valeur("Jean"), "\n")