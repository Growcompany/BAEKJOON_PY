from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
K = int(input())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(K):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(start):
    q = deque()
    q.append(start)
    
    while q:
        node = q.popleft()
        visited[node] = 1
        for a in graph[node]:
            if visited[node] ==0:
                q.append(a)

bfs(1)
print(sum(visited)-1)