import sys

input = sys.stdin.readline

str1 = str(input().rstrip('\n'))
str2 = str(input().rstrip('\n'))
str3 = str(input().rstrip('\n'))

dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]

for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
        for k in range(1,len(str3)+1):
            if str1[i-1] == str2[j-1] and str2[j-1] == str3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1]+1
                #print('i:',i,'j:',j,'k:',k)
                #print('dp[i][j][k]:',dp[i][j][k],'dp[i-1][j-1][k-1]+1:',dp[i-1][j-1][k-1]+1)
            else:
                dp[i][j][k] = max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1],dp[i-1][j-1][k-1])
                

<<<<<<< HEAD
print(dp[len(str1)][len(str2)][len(str3)])
=======
print(dp[len(str1)][len(str2)][len(str3)])
>>>>>>> d132099400117257d56464fc01824e571c32a33f
