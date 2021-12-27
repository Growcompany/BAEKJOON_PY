from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

field = [list(input().strip()) for i in range(12)]

for line in field:
    print(line)

def destory():
    visited = [[0 for _ in range(6)] for _ in range(12)]
    q = deque()
    del_list = []
    boom = False
    for i in range(12):
        for j in range(6):
            if field != '.' and visited[i][j] == 0:
                q.append((i,j,field[i][j]))
                count = 1
                temp = [(i,j)]
                while q:
                    x, y, color = q.popleft()
                    
                    for i in range(4):
                        xx = x+dx[i]
                        yy = y+dy[i]
                        
                        if 0<=xx<12 and 0<=yy<6 and visited[xx][yy] == 0 and field[xx][yy] == color:
                            visited[xx][yy] = 1
                            count +=1
                            temp.append((xx,yy))
                            if count>3:
                                boom = True
                                del_list.append(temp)
                            q.append((xx,yy,color))
    for i in del_list:
        for j in i:
            field[j[0]][j[1]] = '.'
    
    for i in range(6):
        check = False
        if field[11][i] == '.':
            for a in range(10,-1,-1):       
                if not field[a][i] == '.' and check == False:
                    check = True
                    move = 11-a
                if check:
                    field[a+move][i] = field[a][i]
                    field[a][i]= '.'
    return boom

result = 0

while True:
    if destory():
        result +=1
    else:
        print(result)
        break            