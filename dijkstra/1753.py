import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import heapq

INF = int(1e9)

V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V+1)]
distance =[INF]*(V+1) 

for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
    
def dijkstra(start):
    q = []
    distance[start] = 0 
    heapq.heappush(q,(0,start))
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
        
    
dijkstra(start) 

for i in range(1,V+1): 
    print("INF" if distance[i] == INF else distance[i])
