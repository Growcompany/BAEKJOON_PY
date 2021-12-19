from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
room = []

for _ in range(N):
    room.append(list(map(int,input().split())))

q = deque()
q.append((0,1,0)) #현재좌표+현재상태 0은 가로 1은 세로 2은 대각

result = 0
while q:
    a, b, status = q.pop()
    
    if a == N-1 and b == N-1:
        result +=1
        
    if status ==0:
        if b+1<N and room[a][b+1] == 0:
            q.append((a,b+1,0))
            if a+1<N and room[a+1][b+1] == 0 and room[a+1][b] == 0:
                q.append((a+1,b+1,2)) 
    if status ==1:
        if a+1<N and room[a+1][b] == 0:
            q.append((a+1,b,1))
            if b+1<N and room[a+1][b+1] == 0 and room[a][b+1] == 0:
                q.append((a+1,b+1,2)) 
    if status ==2:
        if b+1<N and room[a][b+1] == 0:
            q.append((a,b+1,0))
        if a+1<N and room[a+1][b] == 0:
            q.append((a+1,b,1)) 
            if b+1<N and room[a][b+1] == 0 and room[a+1][b+1] == 0:
                q.append((a+1,b+1,2))
            
print(result)