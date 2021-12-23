from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
room = []
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0]=1

for _ in range(N):
    line = list(map(int,input().split()))
    room.append(line)

for i in range(N):
    for j in range(N):
        move = room[i][j]
        if i==N-1 and j == N-1:
            print(dp[i][j])
            break
        if i+move<N:
            dp[i+move][j] += dp[i][j]
        if j+move<N:
            dp[i][j+move] += dp[i][j]

    
