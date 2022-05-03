
#graph defined by defining adjacent nodes for every node

graph = {
    'A' : ['B', 'C', 'D'],
    'B' : ['A', 'E', 'F'],
    'C' : ['A', 'F'],
    'D' : ['A'],
    'E' : ['B'],
    'F' : ['B', 'C']
    }

startstate = input('Enter start state: ')
goalstate = input('Enter goal state: ')

visited = set()
queue = [startstate]
         
while(len(queue)>0):
    node = queue.pop(0)
    if node not in visited:
        print(node, end = " ")
        if(node == goalstate):
            break
        print('->', end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            queue.append(neighbour)
