def add_edge(src, dest, graph):
    graph[src].append(dest)
    graph[dest].append(src)


def BestFirstSearch(src, goal, v, graph, costs):
    q = [(src, costs[src])]
    visited = [False] * v
    visited[src] = True
    while(len(q)):
        q.sort(key = lambda tup:tup[1])
        f = q[0]
        print(f[0],end=" ")
        q.pop(0)
        if(f[0]==goal): 
            break 
        for i in graph[f[0]]:
            if visited[i]==False:
                q.append((i, costs[i]))
                visited[i] = True


# Driver Code
v = 11
graph = {}
for i in range(v):
    graph[i] = []

add_edge(0, 1, graph)
add_edge(0, 2, graph)
add_edge(0, 3, graph)
add_edge(1, 4, graph)
add_edge(2, 4, graph)
add_edge(2, 5, graph)
add_edge(3, 5, graph)
add_edge(4, 7, graph)
add_edge(5, 6, graph)
add_edge(7, 6, graph)


costs1 = [40, 32, 25, 35, 26, 27, 0, 10]
costs2 = [40, 32, 25, 35, 19, 17, 0, 10]

BestFirstSearch(0, 6, v, graph, costs1)
print()
BestFirstSearch(0, 6, v, graph, costs2)