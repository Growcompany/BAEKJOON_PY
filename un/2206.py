from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int,input().split())
map_list = []
#벽을 한번 부수면 1이되고 여기서 1이상 가면 안되는 걸 체크해야됨.

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    map_list.append(list(map(int,str(input().rstrip('\n')))))
    
def bfs():
    q = deque()
    q.append((0,0,0)) #세번쨰는 뿌신 벽 개수
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    while q:
        x, y, broken = q.popleft()
        
        if x == N-1 and y == M-1:
            return visited[x][y][broken]
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]

            if 0<= xx < N and 0<= yy < M:
                if map_list[xx][yy] ==0 and visited[xx][yy][broken] == 0:
                    visited[xx][yy][broken] = visited[x][y][broken]+1
                    q.append((xx,yy,broken))  
                elif map_list[xx][yy] == 1 and broken == 0:
                    visited[xx][yy][1] = visited[x][y][0]+1
                    q.append((xx,yy,1))
    return -1
           
print(bfs())