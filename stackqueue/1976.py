import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
parent = [i for i in range(N+1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])    
    return parent[x]

def union_parent(x,y):
    x = find_parent(x)
    y = find_parent(y)
    
    if x>y:
        parent[x] = y
    else:
        parent[y] = x
        
for i in range(N):
    line = list(map(int,input().split()))
    for j in range(len(line)):
        if line[j] == 1:
            union_parent(i+1,j+1)
    
tour = list(map(int,input().split()))

result = 'YES'
check_temp = find_parent(tour[0])
for t in tour:
    if check_temp != find_parent(t):
        result = 'NO'
        break

print(result)