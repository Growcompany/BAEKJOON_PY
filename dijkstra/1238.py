import heapq
import sys

input = sys.stdin.readline

N, M, X = map(int,input().rstrip('\n').split())
graph = [[] for _ in range(N+1)]
distance = [1e9 for _ in range(N+1)]
graph_re = [[] for _ in range(N+1)]
distance_re = [1e9 for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int,input().rstrip('\n').split())
    graph[a].append((b,c))
    graph_re[b].append((a,c))
    
def dijkstra(start,graph_type,distance_type):
    distance_type[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    
    while q:
        dis, now = heapq.heappop(q)
        if dis>distance_type[now]:
            continue
        for next_node, next_dis in graph_type[now]:
            if dis+next_dis<distance_type[next_node]:
                distance_type[next_node] = dis+next_dis
                heapq.heappush(q,(dis+next_dis,next_node))
                
dijkstra(X,graph,distance)
dijkstra(X,graph_re,distance_re)
result = 0
for i in range(1,N+1):
    result = max(result, distance[i]+distance_re[i])
print(result)

