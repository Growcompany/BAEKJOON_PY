import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    max_heap = [] #pop을하면 가장 큰 수가 나오게
    min_heap = []
    D_num = 0
    I_num = 0
    for _ in range(N):
        check, num = map(str,input().split())
        num = int(num)
        if check == 'I':
            heapq.heappush(max_heap,-num)
            heapq.heappush(min_heap,num)
            I_num +=1
        else:
            if num == -1: #최솟값 삭제
                if min_heap:
                    heapq.heappop(min_heap)         
            else:
                if max_heap:
                    heapq.heappop(max_heap)
            D_num +=1
    if D_num>I_num:
        print("EMPTY")
    else:
        print(-heapq.heappop(max_heap),heapq.heappop(min_heap))