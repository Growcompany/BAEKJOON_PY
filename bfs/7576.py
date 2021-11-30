from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int,input().split())

tomatoes = []
reds = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    line = list(map(int,input().split()))
    tomatoes.append(line)
    for j in range(len(line)):
        if line[j] == 1:
            reds.append((i,j))
def bfs():
    q = deque()
    for red in reds:
        q.append((red[0],red[1],0))
    result = 0
    while q:
        now_x, now_y,cnt = q.popleft() 
        result = max(result,cnt)
        for i in range(4):
            xx = now_x + dx[i]
            yy = now_y + dy[i]
            if 0 <= xx <N and 0<= yy <M:
                if tomatoes[xx][yy] == 0:
                    tomatoes[xx][yy] = 1
                    q.append((xx,yy,cnt+1))
    return result

print(bfs())
                    
        
    