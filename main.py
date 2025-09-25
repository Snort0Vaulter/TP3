import random
import math
from ex3 import est_positif, affiche_signe, est_bissextile
from constantes import MIN, MAX
from graph import ajouter_noeud, ajouter_arete, parcours_en_profondeur, parcours_en_largeur
from utils import display_graph_from_dict

############################################### EX 4 ###############################################
n = float(input("Entrez un nombre: "))
print("Est positif ?", est_positif(n))
affiche_signe(n)

annee = random.randint(0, 2000)
print("\nAnnée tirée au hasard :", annee)
if est_bissextile(annee):
    print(annee, "est bissextile")
else:
    print(annee, "n'est pas bissextile")


x = random.uniform(MIN, MAX)
print("\nNombre réel tiré au hasard entre", MIN, "et", MAX, ":", x)
print("Signe de son sinus :", end=" ")
affiche_signe(math.sin(x))
############################################### EX 7 ###############################################
graphe = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': [],
    'E': []
}

print("Graphe initial :")
display_graph_from_dict(graphe)
ajouter_noeud(graphe, 'F')           
ajouter_arete(graphe, 'E', 'F')     

print("\nGraphe après ajout de noeud et arête :")
display_graph_from_dict(graphe)
ajouter_arete(graphe, 'A', 'B')

############################################### EX 8 ###############################################
graphe = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': [],
    'E': []
}

print("Parcours en profondeur à partir de A :")
parcours_en_profondeur(graphe, 'A')

print("\nParcours en largeur à partir de A :")
parcours_en_largeur(graphe, 'A')