# -*- coding: utf-8 -*-
class Pile:
	def __init__(self):
		self.pile = []

	def empiler(self, e):
		self.pile.append(e)

	def sommet(self):
		assert len(self.pile) > 0, "Pile vide!"
		return self.pile[-1]

	def depiler(self):
		assert len(self.pile) > 0, "Pile vide!"
		s = self.pile.pop()
		return s

	def estVide(self):
		return len(self.pile) == 0

	def __str__(self):
		retour = ""
		for e in range(len(self.pile)-1, -1,-1):
			retour = retour + str(self.pile[e]) + '\n'
		retour = retour + "====\n"
		return retour


def inverser(pile, nvpile=Pile()):
    if pile.estVide() :
        return nvpile
    else :
        #on supprime le sommet de la pile et on le récupère
        top = pile.depiler()
        #on l'empiler dans la nouvelle pile
        nvpile.empiler(top)
        return inverser(pile, nvpile)

a = Pile()
#création d'une pile contenant 0, 1, 2, 3, 4, 5, 6
for i in range(7):
    a.empiler(i)
#on imprime la pile pour le plaisir
print(a)

a = inverser(a)
print(a)
