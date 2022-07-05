#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

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

    #######################################################
    # non demandé
    #######################################################
    def __str__(self) :
        return str(self.longueur)+" "+str(self.largeur)+" "+str(self.hauteur)


# pour tester la classe
if __name__ == "__main__" :
    #création d'une liste de 20 boîtes
    liste = []
    for i in range(20):
        hauteur = randint(1,30)
        largeur = randint(hauteur,49)
        longueur = randint(largeur,50)
        liste.append(Boite(longueur, largeur, hauteur))

    #vérification
    print("liste non classée")
    for boite in liste:
        print(boite)

    #classement des boîtes du plus grand au plus petit
    def laClef(objet) :
        return objet.longueur, objet.largeur, objet.hauteur
    liste.sort(key = laClef, reverse = True)

    #vérification
    print("Liste classée")
    for boite in liste:
        print(boite)

    #############################################
    # Algorithme glouton
    #############################################
    #liste qui recevra les boîtes emboîtées
    listeEmboitee = [liste[0]]
    #compteur
    i = 1
    while i<len(liste) :
        nouvBoite = liste[i]
        if liste[i].rentreDans(listeEmboitee[len(listeEmboitee)-1]) :
            #la nouvelle boite rentre dans la dernière boite choisie
            listeEmboitee.append(liste[i])
        i = i + 1
    
    #vérification
    print("liste des boites enboitées")
    for i in range(len(listeEmboitee)) :
        print(listeEmboitee[i])
