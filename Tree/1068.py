#너무 내 스타일 야매로 풀었는데 ㅋㅋ 풀리긴하넹
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
Tree = [[] for _ in range(N)]
line = list(map(int,input().split()))
status = [0 for _ in range(N)]
for i in range(len(line)):
    if line[i] != -1:
        Tree[line[i]].append(i)
    
del_node = int(input())
status[del_node] = -1
q = deque([])
for node in Tree[del_node]:
    q.append(node)

while q:
    child = q.popleft()
    status[child] = -1
    for node in Tree[child]:
        q.append(node)
    
count = 0

for i in range(N):
    check = True
    if status[i] != -1:
        if Tree[i]:
            for node in Tree[i]:
                if status[node] == -1:
                    pass
                else:
                    check = False
        if check:
            count +=1
    
print(count)
