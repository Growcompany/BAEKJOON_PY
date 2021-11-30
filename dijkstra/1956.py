import heapq
import sys

input = sys.stdin.readline

V, E = map(int,input().split())
graph = [[1e9]*(V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int,input().split())
    graph[a][b] = c

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

result = 1e9
for i in range(1,V+1):
    if graph[i][i] != 1e9:
        result = min(result,graph[i][i])
    
if result == 1e9:
    print(-1)
else:
    print(result)
                    

            
                
        
    
    
