import sys

input = sys.stdin.readline

R, C, T = map(int,input().split())

room = []
air_c = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(R):
    line = list(map(int,input().split()))
    for j in range(len(line)):
        if line[j] == -1:
            air_c.append((i,j))
    room.append(line)
            
def after_dust(room,length,width):
    q = [] #나중에 더해질 값들을 저장해두는 스택
    for i in range(length): #세로 길이
        for j in range(width): #가로 길이
            if room[i][j] >0:
                div_cnt = 0
                for k in range(4):
                    xx = i+dx[k]
                    yy = j+dy[k]

                    if 0<=xx<length and 0<=yy<width and room[xx][yy]!=-1:
                        div_cnt +=1
                        q.append([xx,yy,int(room[i][j]/5)])
                room[i][j] -= div_cnt*int(room[i][j]/5)
    while q:
        x,y,plus = q.pop()
        room[x][y] +=plus
        
def on_air(room,air_c,length,width):
    up_x = air_c[0][0]
    down_x = air_c[1][0]
    q = []
    #반시계방향으로 돌리기
    for i in range(1,width-1): #->
        q.append((up_x,i+1,room[up_x][i]))
        room[up_x][i] = 0
    for i in range(width-1,0,-1): # <-
        q.append((0,i-1,room[0][i]))
        room[0][i] = 0
    for i in range(up_x,0,-1):
        q.append((i-1,width-1,room[i][width-1]))
        room[i][width-1] = 0
    for i in range(0,up_x-1):
        q.append((i+1,0,room[i][0]))
        room[i][0] = 0
    #시계방향으로 돌리기
    for i in range(1,width-1): #->
        q.append((down_x,i+1,room[down_x][i]))
        room[down_x][i] = 0
    for i in range(width-1,0,-1): # <-
        q.append((length-1,i-1,room[length-1][i]))
        room[length-1][i] = 0
    for i in range(down_x,length-1): #아래로
        q.append((i+1,width-1,room[i][width-1]))
        room[i][width-1] = 0
    for i in range(length-1,down_x+1,-1): #위로
        q.append((i-1,0,room[i][0]))
        room[i][0] = 0
        
    while q:
        x,y,dust = q.pop()
        room[x][y] = dust
        
def count_dust(room,length,width):
    result = 0
    for i in range(length):
        for j in range(width):
            result += room[i][j]
    return result+2
                

length = len(room)
width = len(room[0])

for _ in range(T): 
    after_dust(room,length,width)
    on_air(room,air_c,length,width)

print(count_dust(room,length,width))

    
        