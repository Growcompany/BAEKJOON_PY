import sys
import copy
from collections import deque

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start , end, weight = map(int,input().split())
    graph[start].append((end,weight))
    graph[end].append((start,weight))

start,end = map(int,input().split())

def dfs(now,end,visited,min_weight):
    global result
    #print("now:",now,"end:",end,"visited:",visited,'min_weight:',min_weight)
    if now == end:
        result = max(result,min_weight)
    else:
        for n_node,n_weight in graph[now]:
            if visited[n_node] == False:
                visited[n_node] = True
                dfs(n_node,end,copy.deepcopy(visited),min(n_weight,min_weight))
    
result = 0      
visited = [False]*(N+1)                    
dfs(start,end,copy.deepcopy(visited),1e9)
print(result)
    
    