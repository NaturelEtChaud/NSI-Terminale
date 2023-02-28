# -*- coding: utf-8 -*-
"""
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

def stegano(support,cache,bt):
    '''
    Entrées :
        support : chaîne de caractères donnant le nom de l'image
            avec son extension, qui cachera l'image
        cache : chaîne de caractères donnant le nom de l'image à cacher
        bt : le nombre de bits de poids faible à modifier dans l'image support
    Pré-requis : les 2 images sont de mêmes dimensions
    Sortie : Aucune
    Rôle : l'image finale contiendra sur les bits de poids fort l'image support
        et sur les bits de poids faible l'image cache
    '''
    supp = Image.open(support)
    cach = Image.open(cache)
    largeur , hauteur = supp.size
    #création de l'image
    finale = Image.new("RGB",(largeur,hauteur),"white")
    #traitement
    for x in range(largeur):
        for y in range(hauteur):
            #composante de l'image support
            r_sup, v_sup, b_sup = supp.getpixel((x,y))
            #on supprime les bits de poids faible
            r_sup = masque(r_sup,bt)
            v_sup = masque(v_sup,bt)
            b_sup = masque(b_sup,bt)
            
            #composante de l'image à cacher
            r_cac, v_cac, b_cac = cach.getpixel((x,y))
            #on décale les bits de poids forts vers la droite
            r_cac = r_cac >> (8-bt)
            v_cac = v_cac >> (8-bt)
            b_cac = b_cac >> (8-bt)
            
            #on complète les poids faibles du support
            #par les anciens poids forts de l'image à cacher
            rouge = r_sup | r_cac
            vert = v_sup | v_cac
            bleu = b_sup | b_cac
            
            #on injecte le mélange dans l'image finale
            finale.putpixel((x,y),(rouge,vert,bleu))
    
    #on sauvegarde le résultat
    finale.save('stegano_'+str(bt)+'bits.bmp')
    #on affiche le résultat
    finale.show()
    #on ferme les fichiers
    supp.close()
    cach.close()
    finale.close()

###########################################################
#On fait les images pour des poids faibles allant de 0 à 8.
###########################################################

for bt in range(0,9):
    stegano('cache-cache2.bmp','PIL.bmp',bt)