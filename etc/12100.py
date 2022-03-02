import sys
from collections import deque
import copy
input = sys.stdin.readline

N = int(input())
block = [list(map(int,input().split())) for _ in range(N)]

def move(x,room):
    if x==0: #아래로 밀때 왼쪽하단부터 시작
        for i in range(N):
            index = N-1
            for j in range(N-2,-1,-1):
                if room[j][i]:
                    before_num = room[j][i]
                    room[j][i] = 0
                    if room[index][i] == before_num:
                        room[index][i] *= 2
                        index -=1
                    elif room[index][i] == 0:
                        room[index][i] = before_num
                    else:
                        index -=1
                        room[index][i] = before_num
    elif x==1: #위로 밀때
        for i in range(N):
            index = 0
            for j in range(1,N):
                if room[j][i]:
                    before_num = room[j][i]
                    room[j][i] = 0
                    if room[index][i] == before_num:
                        room[index][i] *=2
                        index +=1
                    elif room[index][i] == 0:
                        room[index][i] = before_num
                    else:
                        index +=1
                        room[index][i] = before_num
    elif x==2: #오른쪽으로 밀때
        for i in range(N):
            index = N-1
            for j in range(N-2,-1,-1):
                if room[i][j]:
                    before_num = room[i][j]
                    room[i][j] = 0
                    if room[i][index] == before_num:
                        room[i][index] *=2
                        index -=1
                    elif room[i][index] == 0:
                        room[i][index] = before_num
                    else:
                        index -=1
                        room[i][index] = before_num
    elif x==3: #왼쪽으로 밀때
        for i in range(N):
            index = 0
            for j in range(1,N):
                if room[i][j]:
                    before_num = room[i][j]
                    room[i][j] = 0
                    if room[i][index] == before_num:
                        room[i][index] *=2
                        index +=1
                    elif room[i][index] == 0:
                        room[i][index] = before_num
                    else:
                        index +=1
                        room[i][index] = before_num
    #for line in room:
    #    print(line)
    #print('------------------------------------')
    return room


def dfs(cnt,room):
    global result
    if cnt == 5:
        max_room = 0
        for line in room:
            max_room = max(max_room,max(line))
        result = max(result,max_room)
    else:
        for i in range(4):
            copy_room = copy.deepcopy(room)
            #print("cnt:",cnt)
            dfs(cnt+1,move(i,copy_room))    

result = 0
dfs(0,block)
print(result)