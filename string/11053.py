import sys

input = sys.stdin.readline

N = int(input())

list_A = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if list_A[i] > list_A[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))
