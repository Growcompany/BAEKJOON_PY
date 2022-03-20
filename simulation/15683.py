import sys
import copy
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
room = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]
directions = [[[0],[1],[2],[3]],[[0,1],[2,3]],[[0,2],[0,3],[1,2],[1,3]],[[0,1,2],[0,1,3],[1,2,3],[0,2,3]],[[0,1,2,3]]] #cctv의 방향을 설정?해주는거 만약에 [0]이면 dx[0],dy[0]해서 왼쪽만 체크 [0,2]면 dx[2],dy[2] 왼쪽이랑 오른쪽보는 방향
cctv = []

for i in range(N):
    line = list(map(int,input().split()))
    for j in range(len(line)):
        if 0<line[j]<6:
            cctv.append([line[j],i,j]) #cctv번호랑 좌표 저장
    room.append(line)

def cctv_on(copy_room,direction,x,y):
    for d in direction:
        xx = x
        yy = y
        
        while True:
            xx += dx[d]
            yy += dy[d]
            if 0<=xx<N and 0<=yy<M and copy_room[xx][yy] != 6:
                copy_room[xx][yy] = '#'
                #print('xx:',xx,'yy:',yy,"copy_room[xx][yy]:",copy_room[xx][yy])
            else:
                break  
    return

def check_zero(room):
    cnt = 0
    for line in room:
        for i in line:
            if i == 0:
                cnt+=1
    return cnt            

def sol(arr,num,copy_room):
    global result
    if num == len(arr):
        result = min(result,check_zero(copy_room))
        return
    for d in directions[arr[num][0]-1]: #arr[num][0]는 몇 번째 카메라인지 체크하는거니까 dir은 0부터 시작이라 1빼줌
        #print("d:",d)
        temp_room = copy.deepcopy(copy_room)
        cctv_on(temp_room,d,arr[num][1],arr[num][2])
        #print('-----------------------------------')
        #for line in temp_room:
        #    print(line)
        #print('-----------------------------------')
        sol(arr,num+1,temp_room)
    return

result = M*N
sol(cctv,0,copy.deepcopy(room))
print(result)
