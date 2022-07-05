#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Eleve :
    ''' classe élèves'''
    
    # le constructeur
    def __init__(self, nom, prenom, ds1, ds2, ds3):
        self.nom = nom
        self.prenom = prenom
        self.notes = [ds1, ds2, ds3]
    
    # méthodes
    def moyenne(self):
        somme = 0
        for i in range(len(self.notes)) :
            somme = somme + self.notes[i]
        return somme / len(self.notes)
    
    
# pour tester la classe
if __name__ == "__main__" :
    hedy =  Eleve("Lamarr", "Hedy", 18, 19, 20)
    print("La moyenne des notes de", hedy.nom, hedy.prenom, "est", hedy.moyenne())
        

