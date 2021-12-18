import sys

input = sys.stdin.readline

N, K = map(int,input().split())
coins = []
dp = [0 for _ in range(K+1)]

for _ in range(N):
    coins.append(int(input()))
    
coins = list(set(coins))

for i in range(1,K+1):
    a = 1e9
    for j in coins:
        if i>=j and dp[i-j] != -1:
            a=min(a,dp[i-j]+1)
    if a == 1e9:
        dp[i] = -1
    else:
        dp[i] = a

print(dp[K])