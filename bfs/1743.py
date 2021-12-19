from collections import deque
import sys

input = sys.stdin.readline

N,M,K = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

room = [[0 for _ in range(M)] for _ in range(N)]
food = []
for _ in range(K):
    a, b = map(int,input().split())
    room[a-1][b-1] = 1
    food.append((a-1,b-1))
    
result =0
def bfs(x,y):
    temp = 0
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = dx[i]+x
            yy = dy[i]+y

            if 0<=xx<N and 0<=yy<M and room[xx][yy] == 1:
                temp+=1
                room[xx][yy] = -1
                q.append((xx,yy))
    return temp
for a in food:
    result = max(result,bfs(a[0],a[1]))
print(result)