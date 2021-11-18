import heapq
import sys

input = sys.stdin.readline

N = int(input())

L_q = []
R_q = []


for i in range(1, N+1):
    num = int(input())
    
    if i%2 == 1:
        heapq.heappush(L_q,-num)
    else:
        heapq.heappush(R_q,num)
    
    if R_q:
        if R_q[0]<-L_q[0]:
            L_q_num = -heapq.heappop(L_q)
            R_q_num = heapq.heappop(R_q)
            heapq.heappush(R_q,L_q_num)
            heapq.heappush(L_q,-R_q_num)
    
    if i%2 == 1:
        print(-L_q[0])
    else:
        print(min(-L_q[0],R_q[0]))