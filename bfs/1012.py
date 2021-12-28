from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]


for _ in range(T):
    M, N, K = map(int,input().split())
    room = [[0 for _ in range(N)] for _ in range(M)]
    visited = [[0 for _ in range(N)] for _ in range(M)]
    q = deque()
    result = 0
    ss = []
    for _ in range(K):
        a, b = map(int,input().split())
        room[a][b] = 1
        ss.append((a,b))

    for s in ss:
        if visited[s[0]][s[1]] ==0:
                q.append((s[0],s[1]))
                result +=1
                visited[s[0]][s[1]] = 1
                while q:
                    x, y = q.popleft()
                    
                    for i in range(4):
                        xx = dx[i]+x
                        yy = dy[i]+y
            
                        if 0<=xx<M and 0<=yy<N and visited[xx][yy] == 0 and room[xx][yy] == 1:
                            visited[xx][yy] = 1
                            q.append((xx,yy))

    print(result)

                
    