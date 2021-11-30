from collections import deque
import sys

input = sys.stdin.readline

K = int(input())
    
def bfs(start):
    visited[start] = 1
    q = deque()
    for move in graph[start]:
        q.append((start,move))
        visited[move] = -1
    while q:
        now, next_n = q.popleft()
        for move in graph[next_n]:
            if visited[move] == 0:
                q.append((next_n,move))
                visited[move] = -visited[next_n]
            elif visited[next_n] == visited[move]:
                return False
    return True
        
for _ in range(K):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    result = True
    for _ in range(E):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0]*(V+1) #0은 미방문, 1은 빨간색이라 가정, -1는 파란색이라 가정
    for i in range(1,V+1):
        if visited[i] == 0:
            if bfs(i) == False:
                print('NO')
                result = False
                break
        
    if result:
        print('YES')   