import sys

input = sys.stdin.readline

N, M = map(int,input().split())

graph = [[1e9]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

min_index = 0
min_result = 1e9
for i in range(1,N+1):
    result = 0
    for j in range(1,N+1):
        result += graph[i][j]
    if min_result > result:
        min_result = result
        min_index = i
        
print(min_index)
    
    