class Boite :
    '''
    boite définie par longueur, largeur, hauteur
    avec longueur >= largeur >= hauteur
    '''
    
    def __init__(self, longueur, largeur, hauteur) :
        assert longueur>=largeur, "la longueur doit être plus grande que la largeur"
        assert largeur>=hauteur, "la largeur doit être plus grande que la hauteur"
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur
    
    def volume(self) :
        return self.longueur * self.largeur * self.hauteur
    
    def rentreDans(self, autre) :
        testLongueur = self.longueur < autre.longueur
        testLargeur = self.largeur < autre.largeur
        testHauteur = self.hauteur < autre.hauteur
        return testLongueur and testLargeur and testHauteur
