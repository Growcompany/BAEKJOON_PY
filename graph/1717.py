import sys

input = sys.stdin.readline
sys.setrecursionlimit(200000)

n,m = map(int,input().split())

parent = [i for i in range(n+1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]
    
def union(x,y):
    x = find_parent(x)
    y = find_parent(y)
    
    if x>y:
        parent[x] = y
    else:
        parent[y] = x
    
for _ in range(m):
    check, a, b = map(int,input().split())
    if check == 1:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a,b)
        
    