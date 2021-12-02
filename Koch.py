from turtle import * # Permet d'importer le module Turtle
from math import sqrt # Permet d'importer la fonction sqrt du module math

# ================ Fonctions de dessin =============

def Koch(long, n) : # Définition de la fonction récurcive Koch
    if n == 0 :
        forward(long)
    else :
        Koch(long/3, n-1)
        left(60)
        Koch(long/3, n-1)
        right(120)
        Koch(long/3, n-1)
        left(60)
        Koch(long/3, n-1)

def Flocon(l, i) : # Définition de la fonction Flocon
    for _ in range(3):
        Koch(l, i)
        right(120)
    
# =============== Programme principal ==============
# ===== Données =====

long = int(input("Choisissez la longueur du flocon : ")) # Input pour avoir la longueur souhaitée par la personne
ite = int(input("Choisissez le nombre d'itération du flocon : ")) # Input pour avoir le nombre d'itération du flocon
x = sqrt((long**2)-((long/2)**2)) # Définition de x avec Pythagore
if ite == 0 : # Condition pour définir le mouvement le point de commencement du dessin sur l'axe y
    deplaY = x/2
else :
    deplaY = x/3

# ===== Paramètrage =====
reset() # Permet de reset Turtle
setup(long+100, x+(x/3)+100) # Setup de la fenetre de Turtle par rapport aux données des Input
title("Flocon de Koch") # Défini le nom de la fenetre
speed(0) # Défini la vitesse de Turtle (0 = instantané)
width(1) # Défini la taille du traie
color("red") # Défini la couleur du traie
# fillcolor("black") # Défini la couleur de remplissage du dessin (si activé)

up() # Permet de lever le crayon
goto(-(long/2),x/3) # Permet d'aller aux coordonnées souhaitées pour rendre le dessin centré
down() # Permet de poser le crayon
ht() # Permet de cacher le crayon/tortue
# begin_fill() # Permet de commencer le remplissage (si activé)
Flocon(long, ite) # Permet de dessiner le Flocon
# end_fill() # Permet de terminer le remplissage (si activé)
exitonclick() # Permet de fermer la fenetre (quand le dessin est terminé) en cliquant dessus
