import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, weight = map(int,input().split())
    graph[a].append((b,weight))
    graph[b].append((a,weight))

start, end = map(int,input().split()) 

def bfs(mid):
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        now = q.pop()
        
        if now == end:
            return True
        
        for n_node, weight in graph[now]:
            if not visited[n_node] and mid>weight:
                visited[n_node] = True
                q.append(n_node)
        
    return False


min_v,max_v = 1, 1_000_000_000

while min_v<=max_v:
    visited = [False]*(N+1)
    mid = (min_v+max_v)//2
    if bfs(mid):
        min_v = mid+1
    else:
        max_v = mid+1
        
print(min_v)