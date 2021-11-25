from collections import deque
import sys

input = sys.stdin.readline

N, M= map(int,input().rstrip('\n').split())
map_list = []

for _ in range(N):
    line = list(map(int,str(input().rstrip('\n'))))
    map_list.append(line)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()
q.append((0,0))

while q:
    x, y = q.popleft()
    
    for i in range(4):
        move_x = x+dx[i]
        move_y = y+dy[i]
        
        if 0<=move_x<N and 0<= move_y<M and map_list[move_x][move_y] == 1:
            map_list[move_x][move_y] = map_list[x][y] +1
            q.append((move_x,move_y))
        
print(map_list[N-1][M-1])
            
    
    

