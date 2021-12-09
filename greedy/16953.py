from collections import deque
import sys

input = sys.stdin.readline

A, B = map(int,input().split())

q = deque()
cnt = 0
result = False
q.append((A,cnt))

while q:
    now, count = q.popleft()
    
    if now<B:
        q.appendleft((int(str(now)+"1"),count+1))
        q.appendleft((now*2,count+1))
    elif now==B:
        result = True
        cnt=count
        break
    
if result:
    print(cnt+1)
else:
    print(-1)