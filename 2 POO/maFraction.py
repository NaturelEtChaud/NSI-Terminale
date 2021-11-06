# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:32:02 2020

@author: Laurent Chaudet
"""

def PGCD(a,b):
    '''
    renvoie le PGCD de a et de b
    autrement le plus grand diviseur commun
    '''
    m = min(abs(a),abs(b))
    #d est le diviseur commun
    #au minimum 1 au maximum m, le minimum entre a et b
    d = 1
    for i in range(2,m+1):
        if (a%i==0 and b%i==0):
            #c'est un diviseur commun
            d = i
    return d


class Fraction :
    '''
    classe  définit par
    - num le numérateur, un entier
    - den le dénominateur, un entier non nul
    '''
    
    #constructeur
    def __init__(self, num, den):
        #vérifications d'usage
        assert den!=0, "on ne peut diviser par zéro"
        assert type(num)==int and type(den)==int, "le numérateur et le dénominateur doivent être des entiers" 
        #signe
        if den < 0 :
            num, den = -num, -den
        #simplification
        d = PGCD(num, den)
        self.num = num//d
        self.den = den//d        
        self.keskc = "fraction"
    
    def numerateur(self):
        '''
        renvoie le numérateur de la fraction
        '''
        return self.num
    
    def denominateur(self):
        '''
        renvoie le dénominateur de la fraction
        '''
        return self.den
    
    def __repr__(self) :
        '''
        affiche la représentation de la fraction
        '''
        return "L'objet est du type "+self.keskc+" et vaut "+str(self.num) + '/' + str(self.den)
    
    def __str__(self) :
        '''
        affiche la fraction sous la forme num/den si den différent de 1
            sinon affiche l'entier num
        '''
        if self.den==1:
            return str(self.num)
        else :
            return str(self.num) + '/' + str(self.den)
    
    def __add__(self, autre) :
        '''
        effectue la somme avec la fraction autre
        '''
        #on utilise le constructeur
        calcul = Fraction(self.num * autre.den + autre.num * self.den , self.den * autre.den )
        return calcul
    
    def __sub__(self, autre) :
        '''
        effectue la différence avec la fraction autre
        '''
        #on utilise le constructeur
        calcul = Fraction(self.num * autre.den - autre.num * self.den , self.den * autre.den )
        return calcul
    
    def __mul__(self, autre) :
        '''
        effectue le produit avec la fraction autre
        autre peut-être une fraction ou un entier
        '''
        #on vérifie que autre est une bien Fraction
        if isinstance(autre, Fraction) :
            calcul = Fraction(self.num * autre.num, self.den * autre.den )
        else :
            #on s'assure quand même que autre est un entier
            assert type(autre)==int, "les nombres doivent être des fractions ou des entiers"
            calcul = Fraction(self.num * autre, self.den )
        return calcul
    
    def __rmul__(self, autre):
        '''
        effectue le produit de autre par la fraction
        '''
        return self.__mul__(autre)

    def __truediv__(self, autre) :
        '''
        effectue le quotient avec la fraction autre
        '''
        #on utilise le constructeur
        calcul = Fraction(self.num * autre.den, self.den * autre.num )
        return calcul
    
    def __pow__(self, exposant):
        '''
        calcule la fraction à la puissance exposant
        '''
        calcul = Fraction(self.num**exposant, self.den**exposant)
        return calcul
    
    def __ge__(self, autre) :
        '''
        renvoie Vrai si la fraction est plus grande que autre
        '''
        #on passe par une mise au même dénominateur
        return (self.num * autre.den >= autre.num * self.den)
    
    def __gt__(self, autre) :
        '''
        renvoie Vrai si la fraction est strictement plus grande que autre
        '''
        #on passe par une mise au même dénominateur
        return (self.num * autre.den > autre.num * self.den)
    
    def __le__(self, autre) :
        '''
        renvoie Vrai si la fraction est plus petite que autre
        '''
        #on passe par une mise au même dénominateur
        return (self.num * autre.den <= autre.num * self.den)
    
    def __lt__(self, autre) :
        '''
        renvoie Vrai si la fraction est strictement plus petite que autre
        '''
        #on passe par une mise au même dénominateur
        return (self.num * autre.den < autre.num * self.den)

    def __eq__(self, autre) :
        '''
        renvoie Vrai si la fraction est égale à l'autre
        '''
        #on fait le produit en croix
        return (self.num * autre.den == autre.num * self.den)
