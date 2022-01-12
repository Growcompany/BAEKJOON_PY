import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split()) #N은 사람수 M은 파티 수
true_num = list(map(int,input().split()))[1:] #진실을 아는 사람들
parent = [i for i in range(N+1)]
party = []
result = 0

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
    
for _ in range(M):
    line = list(map(int,input().split()))[1:]
    line.sort()
    
    for i in range(len(line)-1):
        union_parent(line[i],line[i+1])
    
    if line:
        party.append(line[0])
    else:
        party.append(0)

for i in range(len(true_num)):
    true_num[i] = parent[true_num[i]]

for p in party:
    if find_parent(p) not in true_num:
        result += 1
print(result)