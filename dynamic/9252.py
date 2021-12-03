import sys

input = sys.stdin.readline

s1 = list(str(input().rstrip('\n')))
s2 = list(str(input().rstrip('\n')))

M = len(s2)
N = len(s1)

dp = [[0]*(N+1) for _ in range(M+1)]

for i in range(1,M+1):
    for j in range(1,N+1):
        if s1[j-1] == s2[i-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            
print(dp[M][N])

start_x = M
start_y = N
result_s = []
check_num = dp[M][N]
while True:
    if dp[start_x][start_y] == 0:
        break
    if dp[start_x-1][start_y] == check_num-1 and dp[start_x][start_y-1] == check_num-1:
        start_x -=1
        start_y -=1
        check_num -=1
        result_s.append(s1[start_y])
    elif dp[start_x-1][start_y] == check_num:
        start_x -=1
    elif dp[start_x][start_y-1] == check_num:
        start_y -=1
    
print(''.join(result_s[::-1]))