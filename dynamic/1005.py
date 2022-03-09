import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int,input().split())
    build_time = [0]+list(map(int,input().split()))
    graph = [[] for _ in range(N+1)]
    degree = [0 for _ in range(N+1)]
    dp = [0 for _ in range(N+1)]

    for _ in range(K):
        start, end = map(int,input().split())
        graph[start].append(end) 
        degree[end] +=1
        
    q = deque([])
    
    for i,num in enumerate(degree):
        if num == 0:
            q.append(i)
            dp[i] = build_time[i]
    
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            degree[i] -= 1
            dp[i] = max(dp[i], dp[now]+build_time[i])
            if degree[i] == 0:
                q.append(i)
                
    des = int(input())
    print(dp[des])
    