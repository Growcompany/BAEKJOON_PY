from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int,input().split())
visited = set()
q = deque()
q.append((N,0))

while q:
    now, count = q.popleft()
    if now == K:
        print(count)
        break     
    if not now in visited and abs(now-K)<=abs(N-K):
        q.append((now+1,count+1))
        q.append((now-1,count+1))
        q.append((now*2,count+1))
    visited.add(now)