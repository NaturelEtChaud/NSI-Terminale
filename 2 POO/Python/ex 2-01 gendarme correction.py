#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

liste_grades = ["élève gendarme", "gendarme", "maréchal des logis", "adjudant", "adjudant chef", "major", "élève officier", "sous-lieutenant", "lieutenant", "capitaine", "commandant", "lieutenant colonel", "colonel", "général"]
    

class Gendarme :
    '''
    La super classe des gendarmes à Saint-Tropez
    '''  
    
    # constructeur
    def __init__(self, nom, grade):
        assert isinstance(nom,str), "le nouveau nom n'est pas une chaîne de caractères"
        assert grade in liste_grades, "ce grade n'existe pas"
        self.nom = nom
        self.grade = grade
        self.qi = randint(40,80)
        self.nb_pv = 0
        
    # méthodes
    # les accesseurs et les mutateurs
    def get_nom(self):
        ''' accesseur pour l'attribut nom '''
        return self.nom
    
    def set_nom(self, nouveau_nom):
        ''' mutateur pour l'attribut nom '''
        assert isinstance(nouveau_nom,str), "le nouveau nom n'est pas une chaîne de caractères"
        self.nom = nouveau_nom
    
    def get_grade(self):
        ''' accesseur pour l'attribut grade '''
        return self.grade
    
    def set_grade(self, nouveau_grade):
        ''' mutateur pour l'attribut grade '''
        assert nouveau_grade in liste_grades, "ce grade n'existe pas"
        self.grade = nouveau_grade
 
    def get_qi(self):
        ''' accesseur pour l'attribut qi '''
        return self.qi
    
    def set_qi(self, nouveau_qi):
        ''' mutateur pour l'attribut qi '''
        assert isinstance(nouveau_qi,int) and 40 <= nouveau_qi, "le nouveau qi n'est pas un entier supérieur à 40"
        self.qi = nouveau_qi
    
    def get_nb_pv(self):
        ''' accesseur pour l'attribut nb_pv '''
        return self.nb_pv
    
    def set_nb_pv(self, nouveau_nb_pv):
        ''' mutateur pour l'attribut nb_pv '''
        assert isinstance(nouveau_nb_pv,int) and nouveau_nb_pv >=0, "le nouveau nombre de pv n'est pas un entier positif"
        self.nb_pv = nouveau_nb_pv
    
    # les autres méthodes
    def donner_pv(self) :
        pass
    
    def __str__(self) :
        ''' affiche une belle phrase de présentation dans la console '''
        voyelles = "aeéèếiouy"
        texte = "Bonjour, je suis l"
        if self.grade[0] in voyelles :
            # la première lettre est une voyelle
            texte = texte + "'" + self.grade
        else :
            texte = texte + "e " + self.grade
        texte = texte + " " + self.nom + ", j'ai un qi de " + str(self.qi)
        texte = texte + " et j'ai déjà dressé " + str(self.nb_pv) + " pv."
        return texte
        
    
    
    
