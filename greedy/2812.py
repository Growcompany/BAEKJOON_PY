import sys

input = sys.stdin.readline

N, K = map(int,input().split())
num = list(input())
result = []
del_cnt = K

for i in range(N):
    while del_cnt>0 and result and int(result[-1])<int(num[i]):
        del_cnt -= 1
        result.pop()
    
    result.append(num[i])
    
print(''.join(result[:N-K]))