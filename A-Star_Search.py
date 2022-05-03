
graph = {
    'S' : [['A', 1], ['B', 1]],
    'A' : [['S', 1], ['B', 9]],
    'B' : [['S', 1], ['A', 9], ['C', 6], ['G', 12]],
    'C' : [['B', 6], ['G', 5]],
    'G' : [['C', 5], ['B', 12]]
    }

heuristic = {
    'S' : 7,
    'A' : 10,
    'B' : 9,
    'C' : 5,
    'G' : 0
    }

startstate = input('Enter start state:')
goalstate = 'G'

queue = [[startstate, 0]]

def orderByCost(queue):
    return sorted(queue, key = lambda x: x[1]+heuristic[x[0][-1]])

while(len(queue)>0):
    print(queue)
    currpath, currcost = queue.pop(0)
    if(currpath[-1] == goalstate):
        print("success", "\nPath: ", currpath, " ( Cost=", currcost, ")")
        break
    for node, cost in graph[currpath[-1]]:
        if node in currpath:
            continue
        queue.append([currpath+node, currcost+cost])
    queue = orderByCost(queue)
