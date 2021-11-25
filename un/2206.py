from collections import deque
import sys
import copy

input = sys.stdin.readline

N, M= map(int,input().rstrip('\n').split())
map_list = []
barriers = []
result = []

for i in range(N):
    line = list(map(int,str(input().rstrip('\n'))))
    for j in range(len(line)):
        if line[j] == 1:
            barriers.append([i,j])
    map_list.append(line)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def cal(map_list,change_x,change_y):
    map_l = copy.deepcopy(map_list)
    map_l[change_x][change_y] = 0
    q = deque()
    q.append((0,0))

    while q:
        x, y = q.popleft()

        for i in range(4):
            move_x = x+dx[i]
            move_y = y+dy[i]

            if 0<=move_x<N and 0<= move_y<M and map_l[move_x][move_y] == 0:
                map_l[move_x][move_y] = map_l[x][y] +1
                q.append((move_x,move_y))
    
    if not map_l[N-1][M-1] == 0:    
        result.append(map_l[N-1][M-1]+1)
    
    return
        
if N == 1 and M==1:
    result.append(1)    

for barrier in barriers:
    cal(map_list,barrier[0],barrier[1])
    

print(result)
if len(result) == 0:
    print(-1)
else:
    print(min(result))