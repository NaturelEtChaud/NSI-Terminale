def creer_liste():
	return []

def inserer(liste, element):
	liste.append(element)
	return liste
    
def afficher(liste):
	return liste

l1 = creer_liste()
l1 = inserer(l1, 'Heddy')
l2 = inserer(l1, 'John')
l1 = inserer(l1, 'Ada')
print("l1 =", afficher(l1))
print("l2 =", afficher(l2))