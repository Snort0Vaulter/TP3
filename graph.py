def ajouter_noeud(graphe, noeud):
    """
    ajouter_noeud 

    Parameters : 
    graphe : list
    noeud : list

    Returns : 
    n/a
    """
    if noeud not in graphe:
        graphe[noeud] = []

def ajouter_arete(graphe, source, destination):
    if source not in graphe or destination not in graphe:
        raise ValueError("Les deux noeuds doivent exister dans le graphe.")
    if destination not in graphe[source]:
        graphe[source].append(destination)

def parcours_en_profondeur(graphe, debut):
    a_explorer = [debut]
    deja_visites = []

    while a_explorer:
        n = a_explorer.pop()  
        if n not in deja_visites:
            print(n)           
            deja_visites.append(n)
            for voisin in graphe[n]:
                if voisin not in deja_visites:
                    a_explorer.append(voisin)

def parcours_en_largeur(graphe, debut):
    a_explorer = [debut]
    deja_visites = []

    while a_explorer:
        n = a_explorer.pop(0)  
        if n not in deja_visites:
            print(n)            
            deja_visites.append(n)
            for voisin in graphe[n]:
                if voisin not in deja_visites:
                    a_explorer.append(voisin)