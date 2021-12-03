from collections import deque
import sys

input = sys.stdin.readline

N, k = map(int,input().split())
map_virus=[]
vir_pos = [[] for _ in range(k+1)]

for i in range(N):
    line = list(map(int,input().split()))
    map_virus.append(line)
    for j, num in enumerate(line):
        if num>0:
            vir_pos[num].append((i,j))

second,result_x,result_y = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def virus():
    q=deque()
    time = 0
    for i in range(1,k+1):
        for virus in vir_pos[i]:
            q.append((virus[0],virus[1],i,time))
    while q:
        x,y,num,time = q.popleft()
        if time == second:
            break
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<= xx < N and 0<= yy < N and map_virus[xx][yy] == 0:
                map_virus[xx][yy] = num
                q.append((xx,yy,num,time+1))
    return

virus()

print(map_virus[result_x-1][result_y-1])