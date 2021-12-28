from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

M, N = map(int,input().split())
room = []

for _ in range(M):
    room.append(list(str(input())))

def check(x,y):
    max_dis = 0
    visited = [[0 for _ in range(N)] for _ in range(M)]
    
    q= deque()
    q.append((x,y,0))
    while q:
        a, b, cnt = q.popleft()
        
        for i in range(4):
            xx = dx[i]+a
            yy = dy[i]+b
            
            if 0<=xx<M and 0<=yy<N and room[xx][yy] == 'L' and visited[xx][yy] == 0:
                visited[xx][yy] = cnt+1
                q.append((xx,yy,cnt+1))
    
    for line in visited:
        max_dis = max(max(line),max_dis)
    return max_dis

result = 0
for i in range(M):
    for j in range(N):
        if room[i][j] == 'L':
            result = max(result,check(i,j))

print(result)