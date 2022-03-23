import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())
values = list(map(int,input().split()))
parent = [i for i in range(n+1)]
visited = [False for i in range(n+1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]
    
def union_parent(x,y):
    x = find_parent(x)
    y = find_parent(y)
    
    if x>y:
        parent[x] = y
        values[x-1] = min(values[x-1],values[y-1])
        values[y-1] = min(values[x-1],values[y-1])
    else:
        parent[y] = x
        values[x-1] = min(values[x-1],values[y-1])
        values[y-1] = min(values[x-1],values[y-1])

for _ in range(m):
    a,b = map(int,input().split())
    union_parent(a,b)

cost = 0
for i in range(1,n+1):
    temp_parent = find_parent(i)
    if visited[temp_parent] == False:
        visited[temp_parent] = True
        cost += values[i-1]
    
if k<cost:
    print('Oh no')
else:
    print(cost)
        
        
