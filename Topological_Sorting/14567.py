import sys

input = sys.stdin.readline

N, M = map(int,input().split())

connect = [1 for _ in range(N)]
lec = []

for i in range(M):
    a, b = map(int,input().split())
    lec.append((a-1,b-1))

lec.sort()
for num in lec:
    if connect[num[1]] != 1:
        connect[num[1]] = max(connect[num[1]],1+connect[num[0]])
    else:
        connect[num[1]] +=connect[num[0]]

print(*connect)

#ㅋㅋ이건 내가 야매스타일로 푼거긴해서 살짝 느림
    