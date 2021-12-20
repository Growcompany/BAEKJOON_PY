from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int,input().split())
room = []
shark = []

for i in range(N):
    line = list(map(int,input().split()))
    room.append(line)
    for j in range(len(line)):
        if line[j] == 1:
            shark.append((i,j))

dx = [-1,1,0,0,1,-1,1,-1]
dy = [0,0,-1,1,1,1,-1,-1]

def bfs(a,b):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    result = 0
    q = deque()
    q.append((a,b,0))
    visited[a][b] = 1
    check = True
    while q and check:
        x, y, cnt = q.popleft()
        
        for i in range(8):
            xx = dx[i]+x
            yy = dy[i]+y
            
            if 0<=xx<N and 0<=yy<M and visited[xx][yy] ==0:
                q.append((xx,yy,cnt+1))
                visited[xx][yy] = cnt+1
                if room[xx][yy] == 1:
                    result = cnt+1
                    check = False
                    break
    return result

result = 0
for s in shark:
    result = max(result,bfs(s[0],s[1]))
print(result)