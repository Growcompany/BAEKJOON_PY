from collections import deque
import sys
#늦게 도착하더라도 벽의 개수를 최소화 해야됨
input = sys.stdin.readline

N, M = map(int,input().rstrip('\n').split())
map_list = []

for _ in range(M):
    map_list.append(list(map(int,str(input().rstrip('\n')))))
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[1e9 for _ in range(N)] for _ in range(M)]

q = deque()
q.append((0,0,0))
result = 1e9

while q:
    x, y, broken = q.popleft()
    
    if x==M-1 and y==N-1:
        result = min(result,broken)
    
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        
        if 0<=xx<M and 0<=yy<N:
            if broken < visited[xx][yy]:
                if map_list[xx][yy] == 1:
                    visited[xx][yy] = broken
                    q.append((xx,yy,broken+1))
                else:
                    visited[xx][yy] = broken
                    q.append((xx,yy,broken))
    
print(result)
