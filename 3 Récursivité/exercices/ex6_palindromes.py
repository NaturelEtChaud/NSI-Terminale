# -*- coding: utf-8 -*-

texte = "Éric notre valet alla te laver ton ciré"

def preTraitement(chaine):
    """
    la chaîne de caractères est convertie en minuscule sans les espaces
    """
    modif = chaine.lower()
    modif = modif.replace(' ','')
    return modif

def palindrome_rec(chaine):
    long = len(chaine)
    if long <= 1:
        return True
    else:
        #on prend le premier et le dernier caractères
        pre, der = chaine[0], chaine[-1]
        return (pre == der) and palindrome_rec(chaine[1:long-1])


def palindrome(chaine):
    modif = preTraitement(chaine)
    return palindrome_rec(modif)

print(palindrome(texte))