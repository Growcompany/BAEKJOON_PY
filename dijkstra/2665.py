#bfs 같기도 한디...흠 애매쓰

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
miro = [[] for _ in range(3)] #3차원으로 첫번째 높이의 3차원에는 맵의 좌표 2번째에는 방문햇는지 3번째에는 누적된 벽의 부서진 개수

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    miro[0].append(list(map(int,str(input().rstrip('\n')))))
    miro[1].append([0 for _ in range(N)])
    miro[2].append([0 for _ in range(N)])

q = deque() # 마지막 숫자는 누적된 벽 부서진 개수 만약 이동경로에서 이미 숫자(누적된 부서진 벽의 개수)가 존재한다면 적은 수로 대체 함
q.append((0,0,0))
miro[1][0][0] =1
broken = 0
while q:
    x, y, broken = q.popleft()
    
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        
        if 0<= xx < N and 0<= yy < N:
            if miro[0][xx][yy] == 1:
                if miro[1][xx][yy] == 0: #만약 방문하지 않았던 흰방을 만난다면?
                    miro[1][xx][yy] = 1
                    miro[2][xx][yy] = broken
                    q.append((xx,yy,broken))
                else: #방문했었던 흰방
                    if miro[2][xx][yy] > broken:
                        miro[2][xx][yy] = broken
                        q.append((xx,yy,broken))
                        
            if miro[0][xx][yy] == 0:
                if miro[1][xx][yy] == 0: #만약 방문하지 않았던 검은방을 만난다면?
                    miro[1][xx][yy] = 1
                    miro[2][xx][yy] = broken+1
                    q.append((xx,yy,broken+1))
                else: #방문했었던 검은방
                    if miro[2][xx][yy] > broken+1:
                        miro[2][xx][yy] = broken+1
                        q.append((xx,yy,broken+1))

print(miro[2][N-1][N-1])