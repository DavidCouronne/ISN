#!/usr/local/bin/python
# -*- coding:utf-8 -*-

#Séquence pédagogique ISN: Tri par sélection
#David Couronné


def triSelection(a):
    """prend en entrée une liste a de nombres.
    trie la liste suivant l'algorithme du tri par sélection.
    affiche la longueur de la liste, et le nombre de comparaisons effecuées"""
    n = len(a)
    compteur = 0 #Initialisation du compteur de comparaisons.
    for i in range(n):
        k = i #la selection
        for j in range(i+1, n):
            compteur = compteur + 1 #On va effectuer une comparaison.
            if a[k] > a[j]:
                k = j
            a[k],a[i] = a[i],a[k] #Un moyen d'échanger deux valeurs dans une liste sans passer par une variable auxiliaire.
    print("liste de longeur {} : nombre de comparaisons {}".format(n, compteur))



######
#Implémentation possible de la fonction test_tri
######

from random import randint


def test_tri(n):
    #Utilisation des listes en intension (avec un "s" !):
    liste1 = [i for i in range(n)]
    liste2 = [n-i for i in range(n)]
    liste3 = [randint(0,100) for i in range(n)]
    print("liste ordonnée de {} valeurs: ".format(n))
    triSelection(liste1)
    print("liste ordonnée par ordre décroissant de {} valeurs :".format(n))
    triSelection(liste2)
    print("liste ordonnée de {} valeurs au hasard :".format(n))
    triSelection(liste3)

n = int(input("entrez un nombre d'éléments pour vos listes: "))
test_tri(n)
