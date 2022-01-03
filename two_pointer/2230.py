import sys

input = sys.stdin.readline

N, M = map(int,input().split())
arr =[]

for _ in range(N):
    arr.append(int(input()))
    
arr.sort()

left = 0
right = 0

now = arr[right]-arr[left]
result = 2e9

while right<N:
    now = arr[right]-arr[left]
    if now<M:
        right+=1
    else:
        result = min(result,now)
        left+=1
            
print(result)
    