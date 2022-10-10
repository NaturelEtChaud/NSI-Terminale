#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 18:03:02 2022

@author: loran
"""

############################################################################
#
# La liste chaînée
#
############################################################################


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
    
    def ajouter_tete(self, valeur):
        """ajoute un élément à la liste"""
        self.cellule = Cellule(valeur, self.cellule)
    
    def renvoyer_tete(self):
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
            ord_inverse.ajouter_tete(l.tete)
            l = l.queue
        return ord_inverse
    
    def inserer(self, valeur, position):
        """insére dans la liste une cellule contenant la valeur à la position voulue
        cette position doit être inférieure à la taille de la liste
        """
        assert 0 <= position <= len(self), "erreur d'indexation"
        if position == 0:
            self.ajouter_tete(valeur)
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
            self.renvoyer_tete()
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
            
    def appartient(self, valeur):
        """renvoie vraie si valeur est bien présent dans la liste"""
        if self.est_vide() :
            return False
        else :
            trouve = False
            l = self.cellule
            while l is not None and not trouve:
                if l.tete == valeur :
                    trouve = True
                else :
                    l = l.queue
            return trouve
            
            
############################################################################
#
# La pile
#
############################################################################

class Pile :
    def __init__(self):
        self.data = []
        
    def est_vide(self):
        """renvoie vrai si la pile est vide"""
        return self.data == []
    
    def empiler(self, valeur):
        """empile un nouvel élément à la pile"""
        self.data.append(valeur)
    
    def depiler(self):
        """depile et renvoie l'élément au sommet de la pile"""
        assert self.data != [], "Pile Vide !"
        return self.data.pop()
    
    def sommet(self):
        """renvoie sans le supprimer l'élément au sommet de la pile"""
        assert self.data != [], "Pile Vide !"
        return self.data[-1]
    
    def __str__(self):
        """
        affiche la pile
        la largeur de la pile s'adapte aux nombres de caractères
        nécessaire pour écrire tous les éléments de la pile
        """
        if self.data == []:
            affichage = "| |\n***"
        else :
            affichage = ""
            largeur = max([len(str(e)) for e in self.data])
            for i in range(len(self.data)):
                nb_car = len(str(self.data[-i-1]))
                nb_space = largeur-nb_car
                affichage = affichage + "|"+' '*nb_space+str(self.data[-i-1])+"|\n"
            affichage = affichage + "*"*(largeur+2)
        return affichage
    
    def __len__(self):
        """renvoie la longueur de la pile"""
        return len(self.data)
    
    def echanger(self):
        """enchange les deux éléments du sommet de la pile si elle a au minimum
        2 éléments"""
        assert len(self.data) >=2, "La pile doit avoir au minimum 2 éléments"
        self.data[-2], self.data[-1] = self.data[-1], self.data[-2]
        
    def renverser(self):
        """renverse la pile"""
        self.data = [self.data[-i-1] for i in range(len(self.data))]
    
    def copie(self):
        """crée une copie de la pile"""
        cp = Pile()
        cp.data = self.data.copy()
        return cp
        
        
        
############################################################################
#
# La file
#
############################################################################        
        
        
class File :
    def __init__(self):
        self.data = []
        
    def est_vide(self):
        """renvoie vrai si la file est vide"""
        return self.data == []
    
    def enfiler(self, valeur):
        """enfile un nouvel élément à la file
        l'élément se retrouve à la queue de la file"""
        self.data.append(valeur)
    
    def defiler(self):
        """défile l'élément en tête de file et le renvoie"""
        assert self.data != [], "file Vide !"
        return self.data.pop(0)
        
    def tete(self):
        """renvoie l'élément en tête de file"""
        assert self.data != [], "file Vide !"
        return self.data[0]
    
    def __str__(self):
        """affiche la file, la queue à gauche et la tête à droite"""
        if self.data == []:
            affichage = ">>"
        else :
            affichage = str(self.data[0]) +'>'
            for i in range(1,len(self.data)):
                affichage = str(self.data[i]) + '_' + affichage
            affichage = '>' + affichage
        return affichage
    
    def __len__(self):
        """renvoie la longueur de la file"""
        return len(self.data)
    
    def renverser(self):
        """renverse l'ordre de la file, les premiers seront les derniers"""
        self.data = [self.data[-i-1] for i in range(len(self.data))]
        
    def copie(self):
        """crée une copie de la file"""
        cp = File()
        cp.data = self.data.copy()
        return cp
