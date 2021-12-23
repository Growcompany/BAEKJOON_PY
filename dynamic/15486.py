import sys

input = sys.stdin.readline

N = int(input())
arr = []
dp = [0 for _ in range(N+1)]

for _ in range(N):
    a, b = map(int,input().split())
    arr.append((a,b))

for i,num in enumerate(arr):
    if i+num[0]<=N:
        dp[i+num[0]]= max(dp[i]+num[1],dp[i+num[0]])
    dp[i+1] = max(dp[i+1],dp[i])
        
print(dp[N])