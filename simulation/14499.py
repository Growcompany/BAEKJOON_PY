import sys
import copy
input = sys.stdin.readline

n,m,x,y,k = map(int,input().split())

room = []
cube = {'u':0,'d':0,'e':0,'s':0,'n':0,'w':0}

for _ in range(n):
    line = list(map(int,input().split()))
    room.append(line)
    
command = list(map(int,input().split()))

for c in command:
    check = False
    
    if c == 1:
        if y+1<m:
            y +=1
            temp = copy.deepcopy(cube)
            cube['d'] = temp['e']
            cube['e'] = temp['u']
            cube['u'] = temp['w']
            cube['w'] = temp['d']
            print(cube['u'])
            check = True
    elif c == 2:
        if 0<=y-1:
            y -=1
            temp = copy.deepcopy(cube)
            cube['d'] = temp['w']
            cube['w'] = temp['u']
            cube['u'] = temp['e']
            cube['e'] = temp['d']
            print(cube['u'])
            check = True
    elif c == 3:
        if 0<=x-1:
            x -=1
            temp = copy.deepcopy(cube)
            cube['u'] = temp['s']
            cube['s'] = temp['d']
            cube['d'] = temp['n']
            cube['n'] = temp['u']
            print(cube['u'])
            check = True
    elif c == 4:
        if x+1<n:
            x +=1
            temp = copy.deepcopy(cube)
            cube['d'] = temp['s']
            cube['s'] = temp['u']
            cube['u'] = temp['n']
            cube['n'] = temp['d']
            print(cube['u'])
            check = True
            
    if check:
        if room[x][y] == 0:
            room[x][y] = cube['d']
        else:
            cube['d'] = room[x][y]
            room[x][y] = 0