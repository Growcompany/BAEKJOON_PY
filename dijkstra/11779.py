import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
dis = [1e9 for _ in range(n+1)] 
visited_prev = [-1 for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int,input().split())
    graph[start].append((end,cost))
    
s_node, e_node = map(int,input().split())
result_route = []

def dijkstra(s_node):
    q = []
    heapq.heappush(q,(0,s_node))
    dis[s_node] = 0
    visited_prev[s_node] = s_node
    while q:
        cost, start = heapq.heappop(q)
        if cost>dis[start]:
            continue
        for end_node,plus_cost in graph[start]:
            if dis[end_node] > cost+plus_cost:
                heapq.heappush(q,(cost+plus_cost,end_node))
                dis[end_node] = cost+plus_cost
                visited_prev[end_node] = start
                if end_node == e_node:
                    temp_node = end_node
                    route = []
                    while True:
                        route.append(temp_node)
                        if temp_node == s_node:
                            break
                        temp_node = visited_prev[temp_node]
                    
                    if route:
                        result_route = route.copy()

    print(dis[e_node])
    print(len(result_route))
    print(*result_route[::-1])
    

dijkstra(s_node)
