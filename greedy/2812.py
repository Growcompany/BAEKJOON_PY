import sys

input = sys.stdin.readline

N, K = map(int,input().split())
num = list(str(input()))
result = []

for n in num:  
    while result[-1]<n and K>0:
        K -= 1
        result.pop()
    else:
        break
    result.append(str(n))
    
print(''.join(result))