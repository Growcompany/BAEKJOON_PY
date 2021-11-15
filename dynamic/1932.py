n = int(input())
dp = [[] for _ in range(n+1)]

for i in range(1, n+1):
    list_line = list(map(int, input().split()))
    dp[i] = list_line
    
for i in range(2, n+1):
    for j in range(0, i):
            if j==0:
                dp[i][j] = dp[i-1][j] + dp[i][j]
            elif j ==i-1:
                dp[i][j] = dp[i-1][j-1] + dp[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+dp[i][j]

print(max(dp[n]))