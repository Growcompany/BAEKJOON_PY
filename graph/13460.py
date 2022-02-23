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
    line = list(input())
    for j in range(len(line)):
        if line[j] == 'R':
            red_pos.append(i,j)
        elif line[j] == 'B':
            blue_pos.append(i,j)
    room.append(line)

def bfs(x,y):
    q = deque((x,y,cnt))
    
    while q:
        x, y, cnt = q.popleft()
        
        for i in range(4):
            xx = x
            yy = y
            blue_x = blue_pos[0]
            blue_y = blue_pos[1]
            
            while True:
                xx +=dx[i]
                yy +=dy[i]
                
                if room[xx][yy]
                
            
        
        
    

bfs(red_pos[0],red_pos[1])

    