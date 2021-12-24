import sys

input = sys.stdin.readline

T = int(input())
arr = []
for _ in range(T):
    n = int(input())
    arr.append(n)
    
max_num = max(arr)+1
dp = [1]*max_num
for i in range(2,max_num):
    dp[i] += dp[i-2]
for i in range(3,max_num):
    dp[i] += dp[i-3]

for num in arr:
    print(dp[num])
    