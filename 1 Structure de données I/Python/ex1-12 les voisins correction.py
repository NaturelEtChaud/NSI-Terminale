#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def distance(ptA, ptB):
    """
    Entrées :
        ptA et ptB sont les coordonnées de deux points sous la forme de tuple
    Sortie :
        d est la distance euclidienne entre les points A et B
    """
    d = ((ptA[0] - ptB[0])**2 + (ptA[1] - ptB[1])**2)**0.5
    return round(d,3)

def voisins(k, points, ici):
    """
    Entrées :
        k est le nombre de voisins recherchés
        points est la liste des coordonnées de tous les points
        ici est un tuple contenant les coordonnées d'ici
    Sortie :
        la liste des coordonnées des k plus proches voisins
    """
    # liste de "voisins" bien trop éloignés
    kvoisins = [{"coord": (500,500), "dist": distance(ici,(500,500))} for i in range(k)]
    for p in points :
        # distance au nouveau point
        d = distance(ici, p)
        if d < kvoisins[k-1]["dist"] :
            # p est un meilleur point
            # on le met dans le tableau kvoisins en remontant
            kvoisins[k-1]["coord"] = p
            kvoisins[k-1]["dist"] = d
            i = k-2
            while i >= 0 and d < kvoisins[i]["dist"] :
                  kvoisins[i+1]["coord"], kvoisins[i]["coord"] = kvoisins[i]["coord"],kvoisins[i+1]["coord"]
                  kvoisins[i+1]["dist"], kvoisins[i]["dist"] = kvoisins[i]["dist"], kvoisins[i+1]["dist"]
                  i = i - 1
    reponse = [kvoisins[i]['coord'] for i in range(k)]
    return reponse


liste_points = [(86, -64), (-30, -77), (-34, -43), (-46, 58), (55, -90), (95, 51), 
          (-41, -3), (45, -81), (51, -47), (-1, 42), (-1, 59), (18, 86), (-51, -40),
          (76, -83), (-50, -39), (-73, 81), (-97, 91), (16, 47), (98, 12), (53, 2),
          (-43, -9), (-87, -58), (-31, -94), (32, 25), (-26, 20), (-92, -13),
          (10, -28), (46, -30), (77, 79), (-35, -82), (48, -28), (-100, 82), (9, 3),
          (-82, 68), (84, -53), (-94, -29), (78, -8), (23, -55), (16, 36), (54, 37),
          (-1, 97), (-46, -96), (-94, -91), (-85, 49), (81, -18), (-78, 85), (-71, -20),
          (88, -16), (-33, -38), (-73, -70), (48, 24), (-30, 36), (-68, -81), (98, 12),
          (-28, -18), (-93, -78), (-67, 91), (-64, 52), (-32, -68), (-44, 72), (-26, 38),
          (-32, 73), (55, -56), (-49, 50), (7, 87), (-88, 1), (-33, -5), (-29, 69), (94, 89),
          (-13, -35), (23, -100), (-39, 88), (60, -33), (-54, 73), (-82, -26), (41, -58),
          (63, 5), (-25, -75), (-29, -2), (-24, -44), (-9, 48), (1, -28), (3, -55), (0, 66),
          (-2, -2), (-22, -86), (-93, 20), (95, 10), (-44, 86), (87, -61), (-37, -71), (7, 30),
          (32, -4), (-42, -44), (88, -80), (-94, -75), (-16, 60), (-30, 44), (-22, -14), (89, -41)
          ]
    
assert voisins(3, liste_points, (0,0)) == [(-2, -2), (9, 3), (-22, -14)], "ce ne sont pas les bons voisins"
assert voisins(5, liste_points, (-10,15)) == [(-26, 20), (-2, -2), (9, 3), (7, 30), (-29, -2)], "ce ne sont pas les bons voisins"