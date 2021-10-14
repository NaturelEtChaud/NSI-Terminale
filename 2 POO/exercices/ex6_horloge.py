# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Laurent Chaudet
"""
def rajouterZero(nb):
    '''
    permet de rajouter un 0 si le nombre est plus petit que 10
    '''
    if nb < 10 :
        return "0"+str(nb)
    else :
        return str(nb)


class Horloge :
    '''
    simule une horloge avec la mesure du temps en heure, minute et seconde
    '''

    def __init__(self):
        self.heure = 0
        self.minute = 0
        self.seconde = 0

    #méthodes
    def ticTac(self):
        '''
        rajoute 1 seconde
        '''
        if self.seconde < 59:
            self.seconde += 1
        elif self.minute < 59:
            self.seconde = 0
            self.minute += 1
        else :
            self.seconde = 0
            self.minute = 0
            self.heure += 1

    def reveil(self, h, m, s):
        '''
        sonne le réveil
        '''
        if self.heure == h and self.minute == m and self.seconde == s :
            print("Dring ! Dring !")
            return True
        else :
            return False

    def __repr__(self):
        h = rajouterZero(self.heure)
        m = rajouterZero(self.minute)
        s = rajouterZero(self.seconde)
        return str(h)+"/"+str(m)+"/"+str(s)


#################################################
# On teste la classe
#################################################
monHeure = Horloge()

#et si on se réveillait à 18h14min05s ???
while not monHeure.reveil(18,14,5) :
    print(monHeure)
    monHeure.ticTac()
