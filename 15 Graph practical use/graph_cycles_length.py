matrix1 = []
matrix2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
matrix3 = [[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]]
matrix4 = [[0,1,0,0],[1,0,1,0],[0,0,0,1],[0,0,0,0]]
matrix5 = [[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,1,0,0]]
matrix6 = [[0,1,0,0],[0,0,1,0],[0,0,0,1],[2,0,0,0]]
matrix7 = [[1,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]]

#in oriented from every V in unoriented from one is enough i think
def dfs_cycles(matrix):
    if len(matrix) == 0:
        return []
    min = float('inf')
    for i in range(len(matrix)):
        stack = []
        visited = [False] * len(matrix)
        if dfs(matrix,i,visited,stack):
            if getNumOfEdgesInCycle(stack) < min:
                min = getNumOfEdgesInCycle(stack)
    if min == float('inf'):
        print('No cycle')
        return []
    return min

def getNumOfEdgesInCycle(cycle):    # number of edges in cycle
    if len(cycle) == 0:
        return float('inf')

    first = cycle[0]

    for i in range(1,len(cycle)):
        if cycle[i] == first:
            return i
    return float('inf')

def getCycleLength(matrix, cycle):    # cycle length
    if len(cycle) == 0:
        return float('inf')

    first = cycle[0]
    sum = 0
    for i in range(0,len(cycle)-1):
        if cycle[i] == first and i != 0:
            return sum
        a = cycle[i]
        b = cycle[i+1]
        sum += matrix[cycle[i+1]][cycle[i]]
    return sum



def dfs(matrix,v,visited,stack):
    if visited[v] == True:
        stack.insert(0,v)
        return True
    visited[v] = True
    stack.insert(0,v)
    for i in range(len(matrix)):
        if matrix[v][i]:
            if dfs(matrix,i,visited,stack):
                return True
    visited[v] = False
    stack.pop(0)
    return False

print(dfs_cycles(matrix1))
print(dfs_cycles(matrix2))
print(dfs_cycles(matrix3))
print(dfs_cycles(matrix4))
print(dfs_cycles(matrix5))
print(dfs_cycles(matrix6))
print(dfs_cycles(matrix7))
