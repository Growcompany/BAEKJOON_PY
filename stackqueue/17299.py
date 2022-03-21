import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
line = list(map(int,input().split()))
count = Counter(line)
result = [-1 for _ in range(N)]
s = [0] #처리가 안된 index(?) 번호 그니까 -1인 상태인 index

for i in range(1, N):
    while s and count[line[s[-1]]] < count[line[i]]: #지금까지 누적된 -1인 상태의 최근 값들부터 다 고쳐줌 더 큰 수가 나오면
        index = s.pop()
        result[index] = line[i]
    s.append(i)

print(*result)