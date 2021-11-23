import heapq
import sys

input = sys.stdin.readline

N = int(input())

q = []

for _ in range(N):
    num = int(input().rstrip('\n'))
    if num == 0:
        if len(q) == 0:
            print(0)
        else:
            abs_num, num = heapq.heappop(q)
            print(num)
    else:
        heapq.heappush(q,(abs(num),num))
        