#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image


def coordonnees(nom_photo) :
    """
    Entrées :
        nom_photo est le nom de la photo avec son extension
    Sortie :
        les coordonnées décimales de la prise de vue sous la forme d'un tuple
    """
    photo = Image.open(nom_photo)
    # récupération des métadonnées EXIF
    info = photo._getexif() 		
    # récupération des infos du GPS avec la clef 34853
    gps = info[34853]           
    # récupération des données
    direction_lat = gps[1]
    info_lat = gps[2]
    direction_long = gps[3]
    info_long = gps[4]
    # traitement des données
    lat = info_lat[0][0] + info_lat[1][0]/60 + info_lat[2][0]/3600
    if direction_lat == 'S':
        # hémisphère sud
        lat = lat * (-1)
    long = info_long[0][0] + info_long[1][0]/60 + info_long[2][0]/3600
    if direction_long == 'W':
        # direction ouest
        long = long * (-1)
    return lat, long

coord = coordonnees("chouchou0.jpg")
print(coord)