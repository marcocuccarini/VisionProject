from .graph import *



def dfs1(start, target, path, visited = set()):
    path.append(start)

    visited.add(start)
    if start == target:
    	visited = set()
    	return path
    for neighbour in start.get_connections():
        if neighbour not in visited:
            result = dfs1(neighbour, target, path, visited)
            if result is not None:
            	visited = set()
            	return result
            path.pop()
    visited = set()
    return None

def d(start,target):
	visited = set()
	sumW=0
	res=dfs1(start, target, path=[])
	for i in range(len(res)-1):
		sumW+= res[i].get_weight(res[i+1])
	return sumW







