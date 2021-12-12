import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = list(str(input()))

result = 0
count = 0
pass1 = False
for i in range(1,M-1):
    if pass1:
        pass1 = False
        continue
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        count +=1
        pass1 = True
        if count ==N:
            result +=1
            count -=1
    else:
        count = 0
            
print(result)