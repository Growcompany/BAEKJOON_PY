from collections import deque
from itertools import combinations
import copy
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
map_world = []
virus_pos = []

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if line[j] == 2:
            virus_pos.append((i, j))
    map_world.append(line)
    
dx = [-1,1,0,0]
dy = [0,0, -1, 1]

def virus(map_world, first, second, third):
    world = copy.deepcopy(map_world)
    world[first[0]][first[1]] = 1
    world[second[0]][second[1]] =1
    world[third[0]][third[1]] =1
    count_safe = 0
    for pos in virus_pos:
        q=deque()
        q.append(pos)
        while q:
            xx, yy = q.popleft()
            for i in range(4):
                move_x = xx+dx[i]
                move_y = yy+dy[i]
                if 0<= move_x < N and 0<= move_y <M and world[move_x][move_y] == 0:
                    q.append((move_x,move_y))
                    world[move_x][move_y] = 2
    for line in world:
        count_safe += line.count(0)
    return count_safe

world_pos = []
result =0
for i in range(N):
    for j in range(M):
        world_pos.append((i,j))
list_com = list(combinations(world_pos,3))

for com in list_com:
    trouble = False
    for com_pos in com:
        if map_world[com_pos[0]][com_pos[1]] !=0:
            trouble = True
            break
    if not trouble:
        result = max(virus(map_world,com[0],com[1],com[2]),result)

print(result)