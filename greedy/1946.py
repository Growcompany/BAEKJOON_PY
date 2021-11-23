import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    member=[]
    result = 1
    N = int(input())
    for i in range(N):
        a, b = map(int,input().split())
        member.append([a,b])
    member.sort(key = lambda x:x[0],reverse = False)
    
    cutline = member[0][1]
    for i in range(N):
        if cutline >member[i][1]:
            cutline = member[i][1]
            result +=1
    print(result)
        
        