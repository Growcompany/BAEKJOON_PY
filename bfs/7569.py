from collections import deque
import sys

input = sys.stdin.readline

M, N, H = map(int,input().split())

box = []
tomato = deque([])

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

for i in range(H):
    floor = []
    for j in range(N):
        line = list(map(int,input().split()))
        for k in range(len(line)):
            if line[k] == 1:
                tomato.append([i,j,k]) #k가 가로 j가 세로 i가 높이 
        floor.append(line)
    box.append(floor)

def check_tomato(box):
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 0:
                    return False

    return True
    
def after_oneday(box,result):
    change = False
    global tomato
    plus_tomato = deque([])
    while tomato:
        i, j, k = tomato.popleft()
        for p in range(6):
            xx = dx[p]+i
            yy = dy[p]+j
            zz = dz[p]+k
            
            if 0<=xx<H and 0<=yy<N and 0<=zz<M and box[xx][yy][zz]==0:
                box[xx][yy][zz] = 1
                plus_tomato.append([xx,yy,zz])
                change = True

    tomato = plus_tomato

    if change:
        return True
    else:
        if not check_tomato(box):
            print(-1)
        else:
            print(result)
        return False

result = 0
while after_oneday(box,result):
    result +=1