from collections import deque
import sys

input = sys.stdin.readline

R, C = map(int,input().split())
room = []
S = []
water = []
visited = [[0 for _ in range(C)] for _ in range(R)]

for i in range(R):
    line = list(str(input().rstrip('\n')))
    for j in range(len(line)):
        if line[j] == "S":
            S.append((i,j,0))
        elif line[j] == "*":
            water.append((i,j,1))
    room.append(line)

q = deque(S+water)
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

KAKTUS = True
while q and KAKTUS:
    x,y,type_num = q.popleft() #type_num이 0일땐 S 1일땐 물
    
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<= xx <R and 0<= yy <C:
            if type_num == 0 and room[x][y] == "S":
                if room[xx][yy] == "D":
                    print(visited[x][y]+1)
                    KAKTUS = False
                    continue
                if room[xx][yy] == "." and visited[xx][yy] == 0:
                    room[xx][yy] = "S"
                    visited[xx][yy] = visited[x][y]+1
                    q.append((xx,yy,0))
            if type_num == 1 and (room[xx][yy] =="S" or room[xx][yy] =="."):
                room[xx][yy] = "*"
                q.append((xx,yy,1))
if KAKTUS:
    print("KAKTUS")
    