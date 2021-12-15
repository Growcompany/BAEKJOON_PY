import sys

input = sys.stdin.readline

n, k = map(int,input().split())

graph = []
parent = [x for x in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    a = find(x)
    b = find(y)
    if a>b:
        parent[x] = b
    else:
        parent[y] = a
    return

for _ in range(k):
    start, end, cost = map(int,input().split())
    graph.append((start,end,cost))
    
graph.sort(key = lambda x:x[2])

cycle = False
result = 0

for node in graph:
    if find(node[0]) != find(node[1]):
        union(node[0],node[1])
        result += node[2]

print(result)