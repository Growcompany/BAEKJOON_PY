import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1,N+1):
    graph[i].sort()

def dfs():
    visited = [False]*(N+1)
    q = deque()
    q.append(V)
    while q:
        now = q.popleft()
        if not visited[now]:
            visited[now] = True
            print(now, end = ' ')
            q.extendleft(reversed(graph[now]))

def bfs():
    visited = [False]*(N+1)
    q = deque()
    q.append(V)
    while q:
        now = q.popleft()
        if not visited[now]:
            visited[now] = True
            print(now, end = ' ')
            q.extend(graph[now])
            

dfs()
print()
bfs()
    

