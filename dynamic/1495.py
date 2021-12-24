import sys

input = sys.stdin.readline

N, M, S = map(int,input().split())
arr = list(map(int,input().split()))


dp = [[0 for i in range(S+1)] for _ in range(N+1)]

dp[0][M] = 1

for i in range(N):
    for j,num in enumerate(dp[i]):
        if num==1:
            if j+arr[i]<=S:
                dp[i+1][j+arr[i]]=1
            if j-arr[i]>=0:
                dp[i+1][j-arr[i]]=1
result = -1
for i,num in enumerate(dp[N]):
    if num == 1:
        result = i
print(result)
        