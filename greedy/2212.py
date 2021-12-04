import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

A_list = list(map(int,input().split()))
A_list.sort()

dis = []

for i in range(1,N):
    dis.append(A_list[i]-A_list[i-1])
    
dis.sort(reverse = True)

if N<=K:
    print(0)
else:
    del_dit = dis[K-1:]
    print(sum(del_dit))