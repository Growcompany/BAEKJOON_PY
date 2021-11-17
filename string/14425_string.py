import sys

input = sys.stdin.readline

N, M = map(int, input().split())

S = set()

result = 0

for _ in range(N):
    string = str(input().strip())
    S.add(string)

for _ in range(M):
    string1 = str(input().strip())
    if string1 in S:
        result +=1

print(result)