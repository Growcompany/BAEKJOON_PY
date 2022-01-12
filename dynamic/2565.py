import sys

input = sys.stdin.readline

N = int(input())
towers = [list(map(int,input().split())) for _ in range(N)]
towers.sort()

dp = [1 for _ in range(N)]

for i in range(1,len(towers)):
    for j in range(i):
        if towers[i][1] > towers[j][1]:
            dp[i] = max(dp[i],dp[j]+1)

print(N-max(dp))