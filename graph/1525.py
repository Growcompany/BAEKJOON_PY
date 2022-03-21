#ㅋㅋ visited를 각 숫자마다 각 위치를 방문했느지 체크해서 같은 형태나 안나오게하고 안 겹치게 계속 돌리는 dfs했는데
#그렇게하면 안되는 거가틈.. 아마도 형태가 같은 곳을 여러번 반복해도 중간에 다른곳 들리면 달라지니까 
#이렇게하면안되고 애초에 형태가 겹치는지 체크를하는게 풀이법이었따..

import sys
import copy
from collections import deque

input = sys.stdin.readline

room = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False]*9 for _ in range(9)]
c_room = [[1,2,3],[4,5,6],[7,8,0]]
for i in range(3):
    line =  list(map(int,input().split()))
    for j in range(len(line)):
        if line[j] == 0:
            zero = [i,j]
    room.append(line)

for i in range(3): #각자 본인위치 방문체크
    for j in range(3):
        visited[room[i][j]][i*3+j]=True
        
def dfs(visited,room,x,y,cnt):
    global result
    global c_room
    
    if room == c_room:
        result = min(result,cnt) 
        return
    
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]

        if 0<=xx<3 and 0<=yy<3:
            if not visited[room[x][y]][xx*3+yy] or not visited[room[xx][yy]][x*3+y]:
                print(9999999)
                temp = room[xx][yy]
                room[xx][yy] = 0
                room[x][y] = temp
                visited[room[x][y]][xx*3+yy] = True
                visited[room[xx][yy]][x*3+y] = True
                dfs(copy.deepcopy(visited),copy.deepcopy(room),xx,yy,cnt+1)
            print('------------------')
            for line in room:
                print(line)
result = 1e9
dfs(copy.deepcopy(visited),copy.deepcopy(room),zero[0],zero[1],0)

if result == 1e9:
    print(-1)
else:
    print(result)
                

