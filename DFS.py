graph = {
    'A' : ['B', 'C', 'D'],
    'B' : ['A', 'E', 'F'],
    'C' : ['A', 'F'],
    'D' : ['A'],
    'E' : ['B'],
    'F' : ['B', 'C']
    }
'''
graph2 = {
    0:[1, 3, 8],
    1:[0, 7],
    2:[3, 7, 5],
    3:[0, 4],
    4:[3, 8],
    5:[2, 6],
    6:[5],
    7:[1, 2],
    8:[0, 4]
    }
'''
visited = set()

startstate = input('Enter start state: ')
goalstate = input('Enter goal state: ')

def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        print(node, end="")
        if(node != goalstate):
            print("->", end = "")
            for neighbour in graph[node]:
                dfs(visited, graph, neighbour)
                if(neighbour == goalstate):
                    break
        else:
            exit(0)

dfs(visited, graph, startstate)
