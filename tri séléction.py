#!/usr/local/bin/python
# -*- coding:utf-8 -*-

#Séquence pédagogique ISN: Tri par sélection
#David Couronné

#Implémentation possible des fonctions de l'activité sur le tri par sélection.


def indice_min_liste(liste):
    indice_min = 0 #on initialise
    for i in range(1, len(liste)):
        if liste[i] < liste[indice_min]:
            indice_min = i #si on trouve un élément plus petit, on affecte son indice à indice_min
    return indice_min


#Implémentation classique d'échange de valeurs en passant par une variable temporaire.
#Une implémentation plus efficace en Python est l'utilisation de tuple: a[i], a[j] = a[j], a[i]
def echange_elements(liste, i, j):
    temp = liste[i]
    liste[i] = liste[j]
    liste[j] = temp

#Une implémentation possible. La difficulté principale est la bonne gestion des indices.
def tri_selection(liste):
    longeur_liste = len(liste)
    for i in range(longeur_liste):
        i_min = indice_min_liste(liste[i:]) #On récupère l'indice du minimum à partir de i
        echange_elements(liste, i, i_min+i) #On échange.
        #On peut remarquer ici qu'on échange même si c'est le premier élément qui est le plus petit.
        #L'implémentation n'est pas stable: l'ordre d'apparition des éléments égaux n'est pas préservé.


#Quelques listes pour les tests    
liste1 = [3, 9 , 5, 12, 1,7]
liste2 = [4, 5, 6, 7, 8]
liste3 = [20, 19, 18, 17, 16]


