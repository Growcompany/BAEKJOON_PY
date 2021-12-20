from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int,input().split())

visited = [-1 for _ in range(100001)]
q = deque()
q.append((N,0))
result = [1e9,0]
while q:
    now, cnt = q.popleft()
    
    if now == K:
        if result[0] == cnt:
            result[1] +=1
        elif cnt < result[0]:
            result[0] = cnt
            result[1] = 1
        continue
            
    if visited[now] != -1:
        if visited[now]>=cnt:
            visited[now] = cnt
            if now*2<100001:
                q.append((now*2,cnt+1))
            if now+1<100001:
                q.append((now+1,cnt+1))
            if now-1>=0:
                q.append((now-1,cnt+1))
    else:
        visited[now] = cnt
        if now*2<100001:
            q.append((now*2,cnt+1))
        if now+1<100001:
            q.append((now+1,cnt+1))
        if now-1>=0:
            q.append((now-1,cnt+1))
        
for a in result:
    print(a)    
