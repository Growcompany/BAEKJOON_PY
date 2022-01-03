import sys
import heapq

input = sys.stdin.readline

T = int(input())

def dijkstra(start):
    visited = [-1 for _ in range(n+1)]
    q = []
    heapq.heappush(q,(0,start))
    cnt = 0
    all_time = 0
    
    while q:
        time, start = heapq.heappop(q)
        
        if visited[start] == -1:
            visited[start] = 0
            cnt +=1
            all_time =max(all_time,time)

            for next,plus_time in graph[start]:
                heapq.heappush(q,(time+plus_time,next))
            
    print(cnt,all_time)
    
for _ in range(T):
    n, d, c = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    start = c
    for _ in range(d):
        a, b, s = map(int,input().split())
        graph[b].append((a,s))
    dijkstra(c)