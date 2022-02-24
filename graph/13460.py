import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())
room = []
red_pos = []
blue_pos = []

dx = [-1,1,0,0]
dy = [0,0,1,-1]

for i in range(N):
    line = list(input().rstrip('\n'))
    for j in range(len(line)):
        if line[j] == 'R':
            red_pos.append(i)
            red_pos.append(j)
        elif line[j] == 'B':
            blue_pos.append(i)
            blue_pos.append(j)
    room.append(line)

def bfs(x,y,blue_x,blue_y):
    q = deque([(x,y,blue_x,blue_y,0)])
    visited = []
    visited.append((x,y,blue_x,blue_y))
    cnt = 0
    while q:
        x, y,blue_x,blue_y,cnt = q.popleft()
        
        if cnt>10:
            print(-1)
            return
        
        if room[x][y] == "O":
            print(cnt)
            return
        
        for i in range(4):
            xx = x
            yy = y
            blue_xx = blue_x
            blue_yy = blue_y
            
            while True: # R 계속 움기기 #나올때까지 또는 구멍일떄까지
                xx +=dx[i]
                yy +=dy[i]
                
                if room[xx][yy] == '#':
                    xx -=dx[i]
                    yy -=dy[i]
                    break
                if room[xx][yy] == 'O':
                    break

            while True:  # B계속 움기기 #나올때까지 또는 구멍일떄까지
                blue_xx +=dx[i]
                blue_yy +=dy[i]
                
                if room[blue_xx][blue_yy] == '#':
                    blue_xx -=dx[i]
                    blue_yy -=dy[i]
                    break
                if room[blue_xx][blue_yy] == 'O':
                    break
            
            if room[blue_xx][blue_yy] == 'O': #만약에 파란구슬이 먼저 도착하면 스킵(?)하기
                continue
            
            if xx == blue_xx and yy == blue_yy: #만약 같은 위치까지 이동했다면 더 많이 이동한걸 한칸 돌려놓기
                if abs(x-xx)+abs(y-yy)>abs(blue_x-blue_xx)+abs(blue_y-blue_yy):
                    xx -= dx[i]
                    yy -= dy[i]
                else:
                    blue_xx -= dx[i]
                    blue_yy -= dy[i]
            
            
            if (xx,yy,blue_xx,blue_yy) not in visited:
                visited.append((xx,yy,blue_xx,blue_yy))
                q.append((xx,yy,blue_xx,blue_yy,cnt+1))
                
    print(-1)

bfs(red_pos[0],red_pos[1],blue_pos[0],blue_pos[1])