from collections import deque
import sys

input = sys.stdin.readline

M,N = map(int,input().rstrip('\n').split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
room = []

for _ in range(N):
    room.append(list(str(input().rstrip('\n'))))

W, B =0,0
def bfs(x,y,color):
    temp = 1
    room[x][y] =0
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = dx[i]+x
            yy = dy[i]+y

            if 0<=xx<N and 0<=yy<M and room[xx][yy] == color:
                temp+=1
                room[xx][yy] = 0
                q.append((xx,yy))
    return temp**2

for i in range(N):
    for j in range(M):
        if not room[i][j] == 0:
            if room[i][j] == "W":
                W += bfs(i,j,"W")
            else:
                B += bfs(i,j,"B")
print(W,B)