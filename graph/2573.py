import sys
import copy
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,1,-1]
room = []

for i in range(N):
    line = list(map(int,input().split()))
    room.append(line)
    
def bfs(x,y,visited):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    after = deque()
    while q:
        x, y = q.popleft()
        cnt = 0
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            
            if 0<=xx<N and 0<=yy<M and visited[xx][yy] ==0:
                if room[xx][yy] != 0:
                    visited[xx][yy] =1
                    q.append([xx,yy])
                else:
                    cnt +=1
        if cnt>0:
            after.append([x,y,cnt])
                  
    for x,y,cnt in after:
        room[x][y] = max(0,room[x][y]-cnt) 
    
    #print("---------after---------")
    #for line in room:
    #    print(line)
    #print("---------after---------")
    return

result = 0

while True:
    visited = [[False for _ in range(M)] for _ in range(N)]
    num = 0
    for i in range(N):
        for j in range(M):
            if not room[i][j] == 0 and visited[i][j] == 0:
                bfs(i,j,visited)
                num +=1
    #print('num:',num)
    #print('result:',result)
    if num>1:
        break
    elif num == 0:
        result = 0
        break
    result +=1

print(result)
    