from collections import deque

S = int(input())

imoticon = [[-1]*(S+1) for _ in range(S+1)]

imoticon[1][0] = 0
q = deque()
q.append((1,0))

while q:
    x, y = q.popleft() #xx는 좌표 yy는 클립보드에 저장된 숫자
    if imoticon[x][x] == -1:
        imoticon[x][x] = imoticon[x][y]+1
        q.append((x,x))
    if x+y<=S and imoticon[x+y][y] == -1:
        imoticon[x+y][y] = imoticon[x][y]+1
        q.append((x+y,y))
    if 0<= x-1 and imoticon[x-1][y] == -1:
        imoticon[x-1][y] = imoticon[x][y]+1
        q.append((x-1,y))

result =1e9
for i in range(S):
    if imoticon[S][i] >= 1:
        result = min(imoticon[S][i],result)
print(result)