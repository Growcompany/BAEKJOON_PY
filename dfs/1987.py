import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int,input().split())

room = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(R):
    line = list(input().rstrip('\n'))
    room.append(line)

def bfs(x,y):
    q = deque([(x,y,room[x][y])])
    
    re = 1
    while q:
        x, y, save = q.popleft()
        
        for i in range(4):
            xx =x+ dx[i]
            yy =y+ dy[i]
            
            if 0<=xx<R and 0<=yy<C and (room[xx][yy] not in save):
                q.appendleft((xx,yy,save+room[xx][yy]))
                re = max(re,len(save)+1)

    print(re)

bfs(0,0)