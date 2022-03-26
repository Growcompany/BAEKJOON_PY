import sys
import heapq
input = sys.stdin.readline

n = int(input())
lectures = [list(map(int,input().split())) for _ in range(n)]
lectures.sort(key = lambda x:x[1])
q= []
result = 0
for l in lectures:
    heapq.heappush(q,l[0])
    
    if len(q) > l[1]:
        heapq.heappop(q)
    
print(sum(q))