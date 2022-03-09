import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int,input().split())
    build_time = list(map(int,input().split()))
    graph = [[] for _ in range(N+1)]

    for _ in range(K):
        start, end = map(int,input().split())
        graph[end].append(start) #도착지를 도착하기 위해서 거쳐가야(?) 되는 곳

    des = int(input())
    
    result = 0
    def back_dfs(now,cnt):
        global result
        if not graph[now]:
            result = max(result,cnt)
        for prev_node in graph[now]:
            back_dfs(prev_node,cnt+build_time[prev_node-1])

    
    back_dfs(des,build_time[des-1])
    
    print(result)
    