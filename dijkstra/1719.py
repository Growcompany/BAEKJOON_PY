import sys
import heapq

input = sys.stdin.readline
INF = 1e9
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

result = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    q = []
    distance = [INF]*(n+1)
    distance[start] = 0
    heapq.heappush(q,(0,start))
    path = ['-' for _ in range(n+1)]
    
    while q:
        dist , now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = i[1]+dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
                path[i[0]] = now #이게 원리가 뭐냐면 시작지점에서 도착지점까지 만약에 1에서 4번까지 간다고 쳐봐 근데 여기서 마지막 4번 도착하기전에 3번을 들린다고 치는 지점을 지금 저장한거거든 그러면 반대로 생각해보면 만약 4번에서 1번으로 갈때도 최소 거리로 가려면 3번을 첫번째로 들려서 가야됨. 그래서 마지막 도착 지점 가기전 노드를 저장하면 그건 반대로 루트로 갈 때 첫번째 무조건 들리는 곳이라는 거지
    result[start] = path

for i in range(1,n+1):
    dijkstra(i)
    
for i in range(1,n+1):
    for j in range(1,n+1):
        print(result[j][i], end = ' ')
    print()    
