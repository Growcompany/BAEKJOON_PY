import sys

input = sys.stdin.readline

N, M = map(int,input().split())

parent = [i for i in range(N+1)]

def find_parent(a):
    if parent[a] != a:
        return find_parent(parent[a])
    return parent[a]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

re = False

for i in range(M):
    S_point, E_point = map(int,input().split())
    
    if find_parent(S_point) == find_parent(E_point):
        re = True
        print(i+1)
        break
    
    union_parent(S_point,E_point)

if not re:
    print(0)