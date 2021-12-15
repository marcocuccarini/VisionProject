from .graph import *



def dfs1(start, target, path, visited = set()):
    path.append(start)

    visited.add(start)
    if start == target:
        return path
    for neighbour in start.get_connections():
        if neighbour not in visited:
            result = dfs1(neighbour, target, path, visited)
            if result is not None:
                return result
            path.pop()
    return None

def d(start,target):
    sumW=0
    res=dfs1(start, target, path=[])
    for i in range(len(res)-1):
            sumW+= res[i].get_weight(res[i+1])


    return sumW


def onealldfs(start, alltarget):

    m=0
    
    for i in alltarget:
        
        a=dfs1(start, i, path=[])
        
        if(a>m):

            index=i
            
            m=a

    return (index,m)




