import sys

input = sys.stdin.readline

M, N = map(int,input().split())

list = [False for _ in range(N+1)]

list[1] = True

for i in range(2, int(N**(1/2))+1):
    if list[i]== False:
        for j in range(i*2, N+1, i):
            list[j] = True
    
for i in range(M, N+1):
    if list[i] == False:
        print(i)