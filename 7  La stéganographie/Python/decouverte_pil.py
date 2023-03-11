# -*- coding: utf-8 -*-
"""
@author: Laurent Chaudet
"""

from PIL import Image

#on charge l'image numérique
photo = Image.open('cache-cache.bmp')

#on affiche l'image
photo.show()

#on récupère les dimensions de l'image
largeur , hauteur = photo.size
print(largeur, hauteur)

#récupérer la composante RVB du pixel de coordonnées (120,200)
rouge , vert , bleu = photo.getpixel((190 , 220))
print(rouge, vert, bleu)

#modifier la couleur du pixel de coordonnées (120,200) pour lui donner la couleur (r,v,b)
photo.putpixel((120,200),(255,255,255))

#on affiche le résultat
photo.show()

#on ferme le fichier
photo.close()