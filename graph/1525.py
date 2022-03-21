import sys
from collections import deque
input = sys.stdin.readline

zero = []
visited = {}
room_str = ''

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(3):
    line = str(input().rstrip('\n')).replace(' ', '')
    for j in range(len(line)):
        if line[j] == '0':
            zero = [i,j]
    room_str +=line

def bfs(room_str,x,y):
    q = deque([])
    q.append((room_str,x,y,0))
    while q:
        room_str,x,y,cnt = q.popleft()
        visited[room_str] = True
        
        if room_str == '123456780':
            return cnt
        
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            
            temp_room_str = list(room_str)
            if 0<=xx<3 and 0<=yy<3:
                temp_room_str[x*3+y], temp_room_str[xx*3+yy] = temp_room_str[xx*3+yy], temp_room_str[x*3+y]
                temp_room_str = ''.join(temp_room_str)
                if not temp_room_str in visited:
                    visited[temp_room_str] = True
                    q.append((temp_room_str,xx,yy,cnt+1))
                    
    return -1
                    
print(bfs(room_str,zero[0],zero[1]))
        