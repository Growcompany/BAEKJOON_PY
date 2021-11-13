import sys

input = sys.stdin.readline

N = int(input())

house = [(0,0,0)]
dp = [[0]*3 for _ in range(N+1)]

for _ in range(N):
    R,G,B = map(int, input().split())
    house.append((R,G,B))

for i in range(1,N+1):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2])+house[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2])+house[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1])+house[i][2]

print(min(dp[N][0],dp[N][1],dp[N][2]))