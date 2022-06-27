#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

###################################
# coordonnées de l'ISS
###################################

def coordonnees(url, lycee=True):
    """
    Entrées :
        url l'adresse url de l'api sous la forme d'une chaîne de caractères
        lycee est par défaut True. Si False, on ne passe par le proxy du lycée
    Sortie :
        un tuple contenant les coordonnées terrestres de l'ISS
    """
    if lycee :
        proxy_lycee = {'http':'http://172.30.137.29:3128'}
        lecture = requests.get(url,proxies=proxy_lycee)
    else :
        lecture = requests.get(url)
    ouEstISS = lecture.json()
    long = float(ouEstISS['iss_position']['longitude'])
    lat = float(ouEstISS['iss_position']['latitude'])
    return long, lat


# à la maison
coord = coordonnees('http://api.open-notify.org/iss-now.json', False)
# au lycée
# coord = coordonnees('http://api.open-notify.org/iss-now.json')
print(coord)


###################################
# nombre de personnes dans l'ISS
###################################

def nombres(url, lycee=True):
    """
    Entrées :
        url l'adresse url de l'api sous la forme d'une chaîne de caractères
        lycee est par défaut True. Si False, on ne passe par le proxy du lycée
    Sortie :
        nb est le nombre de personnes actuellement dans l'ISS
    """
    if lycee :
        proxy_lycee = {'http':'http://172.30.137.29:3128'}
        lecture = requests.get(url,proxies=proxy_lycee)
    else :
        lecture = requests.get(url)
    quiEstISS = lecture.json()
    personnes = quiEstISS['people']
    nb = 0
    for p in personnes :
        if p['craft'] == 'ISS':
            nb = nb + 1
    return nb


# à la maison
nb = nombres('http://api.open-notify.org/astros.json', False)
# au lycée
# nb = nombres('http://api.open-notify.org/astros.json')
print(nb)