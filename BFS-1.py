N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
result = 0


def dfs(row, column):
    if row <= -1 or row >= M or column <= -1 or column >= M:
        return False
    if graph[row][column] == 0:
        graph[row][column] = 1
        dfs(row-1, column)
        dfs(row+1, column)
        dfs(row, column+1)
        dfs(row, column-1)
        return True
    else:
        return False


for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)