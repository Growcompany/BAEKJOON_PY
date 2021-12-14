from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int,input().split())

con = [0 for _ in range(N+1)]
arr = [[0] for _ in range(N+1)]
q = deque()

for _ in range(M):
    a, b = map(int,input().split())
    arr[a].append(b)
    con[b] +=1
    
for i in range(1,N+1):
    if con[i] == 0:
        q.append((i))

while q:
    num = q.popleft()
    print(num, end = ' ')
    for i in arr[num]:
        con[i] -= 1
        if con[i] == 0:
            q.append((i))