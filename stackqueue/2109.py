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
    
    if len(q) > l[1]: #그니까 날짜 강의 날짜보다 길이가 길다는건 다 소화를 못한다는거니까 가장 가치가 적은걸 뺴는거임
        heapq.heappop(q)
    
print(sum(q))