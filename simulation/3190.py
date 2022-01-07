from collections import deque
import sys
import copy
input = sys.stdin.readline

N = int(input())
K = int(input())
apples = []

for _ in range(K):
    a, b = map(int,input().split())
    apples.append([a,b])
    
L = int(input())
turns = []

for _ in range(L):
    a, b = list(input().split())
    turns.append((int(a),b))
    
time = 0

#directions = ['L','U','R','D']
temp_dir = 2
snake_head = [1,1]
snake_body = deque([])

while True:
    if snake_head[0] < 1 or snake_head[0] > N or snake_head[1] < 1 or snake_head[1] > N:
        break
    
    if turns and time == turns[0][0]:
        if turns[0][1] == 'L':
            temp_dir +=3
            temp_dir %=4
        else:
            temp_dir +=1
            temp_dir %=4
            
        del turns[0]
    
    food = False
    
    prev = snake_head.copy()
    if temp_dir == 0:
        snake_head[1] =  prev[1]-1
    elif temp_dir == 1:
        snake_head[0] =  prev[0]-1
    elif temp_dir == 2:
        snake_head[1] =  prev[1]+1
    elif temp_dir == 3:
        snake_head[0] =  prev[0]+1
    
    if snake_head in snake_body:
        time +=1
        break
    snake_body.append(prev)
    
    if apples:
        for i in range(len(apples)):
            if snake_head == apples[i]:
                food = True
                del apples[i]
                break
    
    if not food:
        snake_body.popleft()
    time +=1
    
print(time)

