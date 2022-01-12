import sys
from collections import deque
input = sys.stdin.readline

V = int(input())

graph = [[] for _ in range(V+1)]

for i in range(V):
    line = list(map(int,input().split()))
    for j in range(1,len(line)-1,2):
        graph[line[0]].append((line[j],line[j+1]))

def bfs(start):
    visited = [0 for _ in range(V+1)]
    visited[start] = 1
    max_node = 0
    max_dis = 0
    q = deque([])
    
    for end,dis in graph[start]:
        q.append((end,dis))
        visited[end] = 1
        if max_dis<dis:
            max_dis = dis
            max_node = end
    while q:
        start, now = q.popleft()
        
        for end,dis in graph[start]:
            if visited[end] == 0:
                visited[end] = 1
                if max_dis<dis+now:
                    max_dis = dis+now
                    max_node = end
                q.append((end,dis+now))
            
    return max_dis,max_node
    
first_max_dis, first_max_node = bfs(1)
second_max_dis, second_max_node =bfs(first_max_node)
print(second_max_dis)