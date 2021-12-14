from .graph import *

# dfs search modificato
def dfs(start, end):
    visited = {}  # struttura contenete tutti i vertici visitati
    to_visit = set()  # struttura contenente tutti i vertici da visitare
    to_visit.add(start)

    while to_visit:
        # estraggo dalla lista il primo vertice
        next_node = to_visit.pop()
        # esploro i vertici adiacenti a next_node
        for w in next_node.get_connections():
            # se un vertice corrisponde alla fine significa che ho trovato il vertice che cercavo
            if w == end:
                return True
            else:
                if w not in visited:
                    # aggiungo alla lista to_visit tutti i nodi adiacenti a next_node se non sono presenti in visited
                    to_visit.add(w)
            visited[next_node] = next_node
    # nel caso che, finito il while, non ha trovato nessun vertice,
    # questo significa che non è presente, quindi restituisco false
    return False
