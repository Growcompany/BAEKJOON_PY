from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int,input().split())
map_list = [[] for _ in range(3)] #0은 이동가능, 1은 벽 3차원 1차원은 벽의 정보 2차원은 방문체크겸 누적거리

#벽을 한번 부수면 1이되고 여기서 1이상 가면 안되는 걸 체크해야됨.

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    map_list[0].append(list(map(int,str(input().rstrip('\n')))))
    map_list[1].append([1e9 for _ in range(M)])
    map_list[2].append([0 for _ in range(M)])
    
q = deque()
q.append((0,0,1,0)) #세번쨰는 이동거리 네번째는 벽 깨진거 수 세기
result = 1e9
map_list[1][0][0] = 1
while q:
    x, y, move, broken = q.popleft()
    
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        
        if 0<= xx < N and 0<= yy < M and map_list[1][xx][yy] == 1e9:
            if map_list[0][xx][yy] ==0:
                if map_list[1][xx][yy] >= move+1:
                    map_list[1][xx][yy] = move+1
                    if map_list[2][xx][yy] ==1:
                        q.append((xx,yy,move+1,broken))
                        map_list[2][xx][yy] = broken+1
                    else:
                        q.append((xx,yy,move+1,0))
                        map_list[2][xx][yy] = broken+1
            elif map_list[0][xx][yy] == 1:
                if broken <1:
                    if map_list[1][xx][yy] >= move+1:
                        map_list[1][xx][yy] = move+1
                        if map_list[2][xx][yy] ==1:
                            q.append((xx,yy,move+1,broken))
                            map_list[2][xx][yy] = broken+1
                        else:
                            q.append((xx,yy,move+1,0))
                            map_list[2][xx][yy] = broken+1
                    q.append((xx,yy,move+1,broken+1))
                    map_list[2][xx][yy] = broken+1

if map_list[1][N-1][M-1] == 1e9:
    print(-1)
else:                    
    print(map_list[1][N-1][M-1])