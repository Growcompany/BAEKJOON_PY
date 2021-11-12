import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import heapq

INF = int(1e9)

V, E, K = map(int, input().split())

graph = [[] for _ in range(V+1)]
distance =[[INF]*K for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
    
def dijkstra(start):
    q = []
    distance[start][0] = 0 
    heapq.heappush(q,(0,start))
    
    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]][K-1]:
                distance[i[0]][K-1] = cost
                distance[i[0]].sort()
                heapq.heappush(q,(cost, i[0]))
    
dijkstra(1) 

for i in range(1,V+1): 
    print("-1" if distance[i][K] == INF else distance[i][K])
    

