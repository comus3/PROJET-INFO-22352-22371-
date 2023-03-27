

# j'ai tout fait dans une seul fonction contrairement au prof


def findtreasure(plateau):
    def rdfs(i, j, chemin, visites):   #Méthode qui est utilisé Recursive Depth-first search    
        chemin.append((i, j))
        if plateau[i][j].statue == "trésor":
            positions_tresors.append((i, j))
        visites.add((i, j))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(plateau) and 0 <= nj < len(plateau[0]) and plateau[ni][nj].statue != "mur" and (ni, nj) not in visites:
                rdfs(ni, nj, chemin, visites)
        chemin.pop()
        visites.remove((i, j))

    positions_tresors = []  # liste des positions de trésor
    visites = set()  # c'est l'ensemble des cases visitées pour que ça évite les boucles infinies
    for i in range(len(plateau)):
        for j in range(len(plateau[0])):
            if plateau[i][j].statue == "départ":
                rdfs(i, j, [], visites)
    return positions_tresors