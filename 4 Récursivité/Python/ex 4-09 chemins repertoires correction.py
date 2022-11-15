# -*- coding: utf-8 -*-
"""
Created 18/09/20
@author: Guillaume Connan
"""

import os

def printFichiers(chemin: str) -> None:
    if not os.path.isdir(chemin):
        # ce n'est pas un répertoire donc c'est un fichier
        print(chemin)
    else:
        for sous_chemin in os.listdir(chemin):
            printFichiers(chemin + "/" + sous_chemin)