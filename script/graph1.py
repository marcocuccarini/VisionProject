


# La classe Vertex rappresenta i vertici di un grafo
class Vertex:
    # Il costruttore inizializza l’id e il dizionario connectedTo
    def __init__(self, key):
        # id del vertice
        self.id = key
        # dizionario per mantenere traccia dei vertici a cui è connesso e del peso di ogni arco
        self.connected_to = {}

    # Il metodo add_neighbor aggiunge una connessione da questo vertice a un altro
    def add_neighbor(self, nbr, weight=0):
        if nbr not in self.connected_to or weight < self.connected_to[nbr]:
            # Se ci sono archi multipli, salvo il lato di peso minore
            self.connected_to[nbr] = weight

    # Il metodo remove_neighbor rimuove una connessione da questo vertice a un altro
    def remove_neighbor(self, nbr):
        self.connected_to.pop(nbr, None)

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connected_to])

    # Il metodo get_connections ritorna tutti i vertici nella lista di adiacenza,
    # come rappresentato dalla variabile connectedTo
    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    # Il metodo get_weight ritorna il peso di un arco da questo vertice al vertice passato come parametro
    def get_weight(self, nbr):
        return self.connected_to[nbr]


# La classe Graph rappresenta un grafo
# Fornisce metodi per aggiungere vertici a un grafo e connetterli
class Graph:
    def __init__(self):
        # dizionario che mappa gli oggetti vertice
        self.vert_list = {}
        self.num_vertices = 0

    # Il metodo add_vertex aggiunge un vertici al grafo
    def add_vertex(self, key):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    # Il metodo get_vertex ritorna un vertice del grafo
    def get_vertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vert_list

    # Il metodo add_edge aggiunge un lato pesato al grafo
    def add_edge(self, f, t, cost=0):
        if f not in self.vert_list:
            nv = self.add_vertex(f)
        if t not in self.vert_list:
            nv = self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], cost)

    # Il metodo remove_edge rimuove un lato pesato dal grafo
    def remove_edge(self, f, t):
        self.vert_list[f].remove_neighbor(self.vert_list[t])

    # Il metodo get_vertices ritorna i nomi di tutti i vertici nel grafo
    def get_vertices(self):
        return self.vert_list.keys()

    # Il metodo __iter__ permette l’iterazione su tutti i vertici di un grafo dato.
    # Insieme, i due metodi get_vertices e __iter__,
    # permettono di iterare sui vertici di un grafo usando il nome o gli oggetti stessi.
    def __iter__(self):
        return iter(self.vert_list.values())
