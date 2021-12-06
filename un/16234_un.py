from collections import deque
import sys

input = sys.stdin.readline

N, L, R = map(int,input().split())

country = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(N):
    line = list(map(int,input().split()))
    country.append(line)

result = 0

def cal():
    union_count = 0
    visited = [[0]*N for _ in range(N)]
    accu_sum = [0]
    count = [0]
    average = [0]
    for i in range(N):
        for j in range(N):     
            q=deque()
            count[union_count] = 1
            accu_sum[union_count] = country[i][j]
            visited[i][j] = union_count
            q.append((i,j))
            union_country = False
            while q:
                x, y = q.popleft()

                for i in range(4):
                    xx = x+dx[i]
                    yy = y+dy[i]

                    if 0<= xx <N and 0<=yy<N and visited[xx][yy] == 0:
                        if L<=abs(country[x][y]-country[xx][yy])<=R:
                            accu_sum[union_count] +=country[xx][yy]
                            count[union_count] +=1
                            visited[xx][yy] = union_count+1
                            union_country = True
                            q.append((xx,yy))
            if union_country:
                union_count +=1
                accu_sum.append(0)
                count.append(0)
                average.append(0)
                average[union_count] = accu_sum[union_count]//count[union_count]
    
    for a in range(N):
        for b in range(N):
            if visited[a][b] > 0:
                country[a][b] = average[visited[a][b]]
    for line in country:
        print(line)
    if union_count>0:
        result +=1
        cal()
        
cal()
            
print(result)
        
