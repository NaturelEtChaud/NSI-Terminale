# -*- coding: utf-8 -*-
"""
@author: Laurent Chaudet
"""

from PIL import Image
from random import randint

def nouv_image(larg,haut,nom):
    '''
    Entrées : larg et haut sont deux entiers
    Sortie : aucune
    Rôle : création et affichage d'une image de dim (lar,haut)
    Tous les pixels étant choisi au hasard
    '''
    
    #création de l'image
    image = Image.new("RGB",(larg,haut),"white")
    
    #pixels aléatoires sur la nouvelle image
    for x in range(larg):
        for y in range(haut):
            rouge = randint(0,255)
            vert = randint(0,255)
            bleu = randint(0,255)
            image.putpixel((x,y),(rouge,vert,bleu))
    
    #afficahe de l'image
    image.show()
    
    #sauvegarde de l'image
    image.save(nom+".bmp")
    
    #on ferme le fichier
    image.close()