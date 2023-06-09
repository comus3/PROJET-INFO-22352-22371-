class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = 1000
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_adjacent_count(self):#Rajouté par côme pour return le dict de adj
        return len(self.adjacent)

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex
    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous
    """
    def node_exists(graph, node_id):#rajouté par Côme pour savoir si un node existe deja
        for node in graph:
            if node.id == node_id:
                return True
        return False
    """

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

import heapq#c'est la queue

def dijkstra(aGraph, start):
    # Set the distance for the start node to zero 
    start.set_distance(0)
    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v.get_id(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[2]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
            else:
                continue

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v.get_id(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)



####### SOURCE   :   https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php
####### Je pense que l'article date de il y a longtemps donc heapq marche légèrement différemment
####### donc quand on faut un heapify, il veut comparer deux vertex et il est pas content donc je vais 
####### rajouter des comparateurs dans la classe vertex

####### AUTRE SOLUCE:
####### comme heap va comparer le premier elem du tuple et si egaux il va comparer le deuxieme ,ect
####### jai juste rajouté le id du vertex au tuple vu qu'ils sont tous différents donc quand poids identiques
####### il va comparer id et va le trier dans cet ordre
#######
#######INFO: dijkstra ne sert plus a rien mtn que je me rends compte de ma betise immense. on eput se deplacer de plus dune case
#######      a la fois donc chercher le chemin le plus court na plus aucun interet pour linstant
#######
#######FINAL NOTE: Le fichier dijkstra contient les methodes nécéssaires au calul de la portée de l'énemi
####### en effet, on calcule le graphe apt de la pos de l'enemi et on fait la somme des distances