import sys

input = sys.stdin.readline

N, K = map(int,input().split())

dp =[[1 for _ in range(K)] for _ in range(N)]

for a in range(K):
    dp[0][a] = a+1
for i in range(1,N):
    for j in range(1,K):
        dp[i][j] = (dp[i-1][j]+dp[i][j-1])%1e9
    
print(int(dp[N-1][K-1]))