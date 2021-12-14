import sys

input = sys.stdin.readline

n, k = map(int,input().split())
coins = []
dp = [0 for _ in range(k+1)]
dp[0] = 1
for _ in range(n):
    coins.append(int(input()))
    
for coin in coins:
    for j in range(coin,k+1):
        dp[j] += dp[j-coin]
    
print(dp[k])