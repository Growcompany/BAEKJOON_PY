import sys

input = sys.stdin.readline

N, S = map(int,input().split())
arr = list(map(int,input().split()))

start = 0
end = 1
temp_sum = sum(arr[0:end])

result = 1e9

while True:
    if temp_sum>=S:
        if start+1 == end:
            result = 1
            break
        else:
            result = min(result, end-start)
            temp_sum -= arr[start]
            start+=1
    else:
        if end == N:
            break
        else:
            end +=1
            temp_sum += arr[end-1]

if result == 1e9:
    print(0)
else:
    print(result)