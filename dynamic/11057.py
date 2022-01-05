import sys

input = sys.stdin.readline

N = int(input())

dp = [[1 for _ in range(10)] for _ in range(N)]

for i in range(1,N):
    for j in range(1,10):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]

print(int(sum(dp[N-1])%10007))