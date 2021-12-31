import sys

input = sys.stdin.readline

N = int(input())
graph = []
edges = []
parent = [i for i in range(N)]
result=0

for i in range(N):
    a,b,c = map(int,input().split())
    graph.append((a,b,c,i))

for i in range(3):
    graph.sort(key = lambda x:x[i])
    for j in range(N-1):
        edges.append((abs(graph[j][i]-graph[j+1][i]),graph[j][3],graph[j+1][3]))
        
edges.sort()

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a>b:
        parent[a] = b
    else:
        parent[b] = a
        
for edge in edges:
    if find_parent(edge[1]) != find_parent(edge[2]):
        union_parent(edge[1],edge[2])
        result += edge[0]
        
print(result)