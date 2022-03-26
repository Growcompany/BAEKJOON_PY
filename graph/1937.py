import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
dp = [[1 for _ in range(n)] for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

room = [list(map(int,input().split())) for _ in range(n)]

def dfs(x,y):
    if dp[x][y] >1:
        return dp[x][y]
    else:
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            
            if 0<=xx<n and 0<=yy<n and room[x][y] < room[xx][yy]:
                dp[x][y] = max(dp[x][y], dfs(xx,yy)+1)
    return dp[x][y]
    
result =1
for i in range(n):
    for j in range(n):
        result = max(result,dfs(x,y))
print(result)