import sys
import heapq

input = sys.stdin.readline

N, K = map(int,input().split())
je = []
bag = []
for _ in range(N): #각 보석의 정보받기
    M, V = map(int,input().split())
    je.append([M,V])
    
for _ in range(K): #각 가방의 최대무게
    weight = int(input())
    bag.append(weight)
    
je.sort()
bag.sort()
result = 0
heapq.heapify(je)
q = []

for num in bag:
    while je and num>=je[0][0]:
        heapq.heappush(q,-heapq.heappop(je)[1]) #힙은 최소힙을 먼저 pop하므로 음수로 바꿔서 
    if q:
        result -= heapq.heappop(q)
    if not je:
        break
    
print(result)
    
    