# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 13:38:01 2020

@author: Laurent Chaudet
"""

from PIL import Image

def masque(nb,bt) :
    '''
    Entrées :
        nb est un nombre entier entre 0 et 255
        bt est un nombre enter entre 0 et 8
    Sortie : un nb entier
    Rôle : on supprime les bt bits de poids faible à l'aide d'un masque
    '''
    mask = 0
    for i in range(bt,8):
        mask = mask + 2**i
    return nb & mask


def image_faible(nom,bt):
    '''
    Entrées :
        nom est le nom de l'image avec son extension
        bt est un nombre entier entre 0 et 8
    Sortie : aucune
    Rôle : on supprime les bt bits de poids faible de chaque
    composante rouge, vert, bleu de chaque pixel
    '''
    photo = Image.open(nom)
    largeur , hauteur = photo.size
    for x in range(largeur):
        for y in range(hauteur):
            rouge , vert , bleu = photo.getpixel((x,y))
            #on supprime les bits de poids faible
            rouge = masque(rouge,bt)
            vert = masque(vert,bt)
            bleu = masque(bleu,bt)
            #on réinjecte la nouvelle composante
            photo.putpixel((x,y),(rouge,vert,bleu))
    #on sauvegarde le résultat
    photo.save('poids_faible'+str(bt)+'.bmp')
    #on affiche le résultat
    photo.show()
    #on ferme fichier
    photo.close()

###########################################################
#On fait les images pour des poids faibles allant de 0 à 8.
###########################################################

for bt in range(0,9):
    image_faible('cache-cache.bmp',bt)

    


    