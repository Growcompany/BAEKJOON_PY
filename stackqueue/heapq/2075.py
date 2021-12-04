import heapq
import sys

input = sys.stdin.readline

N = int(input())
q = []

for _ in range(N):
    line = list(map(int,input().rstrip('\n').split()))
    for num in line:
        if len(q) < N:
            heapq.heappush(q,num)
        if q[0] < num:
            heapq.heappop(q)
            heapq.heappush(q,num)
        
print(heapq.heappop(q))