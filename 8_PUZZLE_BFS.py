import copy
import time 

def getNext(node):
    global nextStates
    nextStates = []
    for row in range(0, len(node)):
        for col in range(0, len(node[row])):
            if(node[row][col]=='_'):
                break
        else:
            continue
        break

    if(row==0 or row==1):
        a = copy.deepcopy(node)
        a[row][col], a[row+1][col] = a[row+1][col], a[row][col]
        nextStates.append(a)

    if(row==1 or row==2):
        a = copy.deepcopy(node)
        a[row][col], a[row-1][col] = a[row-1][col], a[row][col]
        nextStates.append(a)
    
    if(col==0 or col==1):
        a = copy.deepcopy(node)
        a[row][col], a[row][col+1] = a[row][col+1], a[row][col]
        nextStates.append(a)

    if(col==1 or col==2):
        a = copy.deepcopy(node)
        a[row][col], a[row][col-1] = a[row][col-1], a[row][col]
        nextStates.append(a)
    return nextStates


'''Driver Code''' 

# Creating start and goal state

startstate =[[1, 2, 3],
             ['_', 5, 6],
             [4, 7, 8]]
goalstate = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, '_']]


visited = []
queue = [startstate]
nextStates = []

# Starting Timer
start = time.time()
while(len(queue) > 0):
    if(len(queue) > 100):
        break
    node = queue.pop(0)
    neighbours = getNext(node)
    if node not in visited:
        print(node, end = " ")
        if(node == goalstate):
            break
        print('\n\n<------------------ 🡫 ------------------>\n')
        visited.append(node)
        for neighbour in neighbours:
            queue.append(neighbour)


# Closing Timer
end = time.time()

print("Total Time Taken: ", end - start)