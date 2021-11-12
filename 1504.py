import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import heapq

INF = int(1e9)

V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
    
def dijkstra(start, end):
    distance =[INF]*(V+1) 
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
    return distance[end]

def solve():
    v1, v2 = map(int, input().split())

    result1 = dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,V)
    result2 = dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,V)
    print(-1 if min(result1,result2) >= INF else min(result1,result2))

solve()
