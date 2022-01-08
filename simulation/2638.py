import sys
from collections import deque 

input = sys.stdin.readline

N, M = map(int,input().split())
room = []
chz = []
time = 0

for i in range(N):
    line  = list(map(int,input().split()))
    for j in range(M):
        if line[j] == 1:
            chz.append((i,j))
    room.append(line)

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def out_line(a,b):
    q = deque([])
    q.append((a,b))
    
    while q:
        print('c')
        x, y =q.popleft()
        
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            
            if 0<=xx<N and 0<=yy<M and room[xx][yy] == 0:
                room[xx][yy] = 2
                q.append((xx,yy))

while chz:
    del_chz = []
    
    for x,y in chz:
        check = 0
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<N and 0<=yy<M and room[xx][yy] == 2:
                check +=1
        if check>=2:
            del_chz.append((x,y))
            
    for chz_x,chz_y in del_chz:
        room[chz_x][chz_y] = 0

    for chz_x,chz_y in del_chz:
        if room[chz][chz_y] == 0:
            out_line(chz_x,chz_y)
        
    chz = [x for x in chz if not x in del_chz]
    
    time +=1

print(time)
    