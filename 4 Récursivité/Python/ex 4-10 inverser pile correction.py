from TAD import Pile

def inverser(pile ,nouvelle_pile = Pile()):
	if pile.est_vide() :
		return nouvelle_pile
	else :
		top = pile.depiler()
		nouvelle_pile.empiler(top)
		return inverser(pile, nouvelle_pile)





a = Pile()
# création d'une pile contenant 0, 1, 2, 3, 4, 5, 6
for i in range(7):
	a.empiler(i)
# on imprime la pile pour le plaisir
print(a)

b = inverser(a)
print(b)
