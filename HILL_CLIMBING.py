def add_edge(src, dest, graph):
    graph[src].append(dest)
    graph[dest].append(src)


def HillClimbing(src, goal, v, graph, costs):
    q = (src, costs[src])
    visited = [False] * v
    visited[src] = True
    while(True):
        print(q[0], end=" ")
        if(q[0] == goal): 
            return   
        next_cost = costs[q[0]]
        next = q[0]
        exists = False
        for i in graph[q[0]]:
            if visited[i] == False and (costs[i] <= next_cost):
                next_cost = costs[i]
                next = i
                exists = True
                visited[i] = True
        if not exists:
            return
        q=(next, next_cost)


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

HillClimbing(0, 6, v, graph, costs1)
print()
HillClimbing(0, 6, v, graph, costs2)