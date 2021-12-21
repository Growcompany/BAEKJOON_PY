from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int,input().split())
room = []
shark = deque()

for i in range(N):
    line = list(map(int,input().split()))
    room.append(line)
    for j in range(len(line)):
        if line[j] == 1:
            shark.append((i,j))

dx = [-1,1,0,0,1,-1,1,-1]
dy = [0,0,-1,1,1,1,-1,-1]

def bfs(a,b):
    while shark:
        x, y = shark.popleft()
        for i in range(8):
            xx = dx[i]+x
            yy = dy[i]+y
            
            if 0<=xx<N and 0<=yy<M and room[xx][yy] ==0:
                shark.append((xx,yy))
                room[xx][yy] = room[x][y]+1
    return

result = 0
for i in range(N):
    for j in range(M):
        result = max(result,room[i][j])
print(result)