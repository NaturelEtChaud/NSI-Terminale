def creer_liste():
	return ()

def inserer(liste, element):
	return (element, liste)
	
def afficher(liste):
	reponse = []
	while liste != ():
		tete, liste = liste
		reponse.append(tete)
	return reponse

l1 = creer_liste()
l1 = inserer(l1, 'Heddy')
l2 = inserer(l1, 'John')
l1 = inserer(l1, 'Ada')
print("l1 =", afficher(l1))
print("l2 =", afficher(l2))