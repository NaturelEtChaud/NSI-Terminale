from turtle import *
shape("turtle")

#longueur de la coure
l = 243
#nombre d'appels récursif
n = 4


#la fonction définie par récursivité
def koch(n,l):
    if n == 0:
        forward(l)
    else:
        koch(n-1, l/3)
        left(60)
        koch(n-1, l/3)
        right(120)
        koch(n-1, l/3)
        left(60)
        koch(n-1, l/3)


#on positionne la tortue
up()
right(180)
forward(l/2)
right(180)
down()

#c'est parti pour faire un beau dessin
koch(n,l)

#pour fermer proprement
exitonclick()
done()