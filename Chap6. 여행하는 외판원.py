n=input(()) # 도시의 수
dist=[] # 두 도시간의 거리를 저장하는 리스트


def shortestPath(path, visited, currentLength):
    if len(path) == n:
        return currentLength + dist[path[0]][path.pop()]
    
    ret= 987654321

    for next in range(n):
        if visited[next] :
            continue
        else:
            here = path.pop()
            path.append(next)
            visited[next] = True
        cand = shortestPath(path, visited, currentLength+dist[here][next])

        ret = min(ret, cand)
        visited[next] = False
        del path[-1]
    
    return ret