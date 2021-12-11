import sys

input = sys.stdin.readline

N, M = map(int,input().split())
list_num = list(map(int,input().split()))

start = 0
end = 0
result = 0

while start < N and end < N:
    if sum(list_num[start:end+1]) < M:
        end += 1
    elif sum(list_num[start:end+1]) > M:
        start += 1
    else:
        result += 1
        if start == end:
            end += 1
        else:
            start += 1

print(result)