N = int(input())
dp = [0 for _ in range(N+1)]
dp[0] = 1

if N%2 == 0:
    for i in range(2,N+1,2):
        if i-3>0:
            for j in range(0,i-3,2):
                dp[i] += dp[j]*2
        dp[i] += dp[i-2]*3
    print(dp[N])
else:
    print(0)