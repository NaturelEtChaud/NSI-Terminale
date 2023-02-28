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
    Rôle : on supprime les bt bits de poids fort à l'aide d'un masque
    et on décale vers la gauche d'autant de bits
    '''
    mask = 0
    for i in range(0,8-bt):
        mask = mask + 2**i
    return (nb & mask) << bt

def destegano(support,bt):
    '''
    Entrées :
        support : chaîne de caractères donnant le nom de l’image
            avec son extension, qui cache l’image
        bt : le nombre de bits de poids faible modifiée dans l’image support
    Sortie : Aucune
    Rôle : l’image finale contiendra sur les bits de poids fort l’image support
        et sur les bits de poids faible l’image cache
    '''
    supp = Image.open(support)
    largeur , hauteur = supp.size
    #création de l'image
    finale = Image.new("RGB",(largeur,hauteur),"white")
    #traitement
    for x in range(largeur):
        for y in range(hauteur):
            #composante de l'image support
            rouge, vert, bleu = supp.getpixel((x,y))
            #on supprime les bits de poids forts et on décale
            rouge = masque(rouge,bt)
            vert = masque(vert,bt)
            bleu = masque(bleu,bt)
            
            #on injecte la modification dans l'image finale
            finale.putpixel((x,y),(rouge,vert,bleu))
    
    #on sauvegarde le résultat
    finale.save('déstegano_'+str(bt)+'bits.jpg')
    #on affiche le résultat
    finale.show()
    #on ferme les fichiers
    supp.close()

    finale.close()

###########################################################
#On fait les images pour des poids faibles allant de 0 à 8.
###########################################################

for bt in range(0,9):
    destegano('cache-cache-surprise.bmp',bt)
