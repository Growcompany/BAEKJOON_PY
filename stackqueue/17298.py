import sys

input = sys.stdin.readline

N = int(input().rstrip('\n'))

list_num = list(map(int,input().rstrip('\n').split()))

result = [-1]*N
stack = [0] #처리해야될 인덱스 넘버 처음에는 0번째꺼 처리해야 됨

for i in range(1,N):
    while stack and list_num[stack[-1]] < list_num[i]:
        result[stack.pop()] = list_num[i]
    stack.append(i)

print(*result)
