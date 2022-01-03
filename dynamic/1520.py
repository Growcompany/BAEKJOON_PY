import heapq
import sys

input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [-1,1,0,0]

M, N = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]

q = []
heapq.heappush(q,(-room[0][0],0,0))
visited[0][0] = 1

while q:
    cnt, x, y = heapq.heappop(q)
    if x==M-1 and y==N-1:
        continue
        
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        
        if 0<=xx<M and 0<=yy<N and room[xx][yy]<room[x][y]:
            if visited[xx][yy]==0:
                heapq.heappush(q,(-room[xx][yy],xx,yy))
            visited[xx][yy] += visited[x][y] 

print(visited[M-1][N-1])
            