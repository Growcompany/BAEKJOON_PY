from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int,input().split())

visited = [-1 for _ in range(100001)]
q = deque()
q.append((N,0))
result = 0
re = deque([])
while q:
    now, cnt = q.popleft()
    
    if now == K:
        result = cnt
        break
            
    if visited[now] == -1:
        if now*2<100001:
            visited[now*2] = now
            q.append((now*2,cnt+1))
        if now+1<100001:
            visited[now+1] = now
            q.append((now+1,cnt+1))
        if now-1>=0:
            visited[now-1] = now
            q.append((now-1,cnt+1))

num = K
while True:
    if num == N:
        break
    re.appendleft(num)
    num = visited[num]
print(result)
print(*re)