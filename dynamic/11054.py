import sys

input = sys.stdin.readline

N = int(input())

list_A = list(map(int, input().split()))

dp = [1 for _ in range(N)]
dp_reverse = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if list_A[i] > list_A[j]:
            dp[i] = max(dp[i],dp[j]+1)
            
list_A.reverse()

for i in range(1, N):
    for j in range(i):
        if list_A[i] > list_A[j]:
            dp_reverse[i] = max(dp_reverse[i],dp_reverse[j]+1)

dp_reverse.sort()
result = 0
print(dp)
print(dp_reverse)
for i in range(0,N):
    result = max(result,dp[i]+dp_reverse[i])
    
print(result-1)