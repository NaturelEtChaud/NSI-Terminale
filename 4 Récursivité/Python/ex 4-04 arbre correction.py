from turtle import *
shape("turtle")
speed(0.1)

#longueur du tronc
l = 200
#angle de l'inclinaison de la branche
o = 30
#rapport entre branche et tronc
r = 1/2
#nombre d'appels récursif
n = 5


#la fonction définie par récursivité
def arbre(n,l,r,o):
    color('brown')
    if n == 0:
        color('green')
        forward(l)
        right(180)
        forward(l)
        color('brown')
    else:
        #le tronc
        forward(l)
        #la branche à droite
        right(o)
        arbre(n-1,l*r,r,o)
        #la branche à gauche
        right(180-2*o)
        arbre(n-1,l*r,r,o)
        #retour à la base du tronc
        right(o)
        forward(l)



#on positionne la tortue
up()
right(90)
forward(l)
down()
left(180)

#c'est parti pour faire un beau dessin
arbre(n,l,r,o)


#pour fermer proprement
exitonclick()
mainloop()