from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

q = deque()
q.append(N)

position = [-1 for _ in range(100001)]
position[N] = 0


while q:
    N_now = q.popleft()
    if N_now == K:
        print(position[K])
        break
    if 0<= N_now-1 <=100000 and position[N_now-1] == -1: #만약 N이 K보다 커서 작은 수부터 나올 수도 있음
        position[N_now-1] = position[N_now]+1
        q.append(N_now-1)
    if 0<= N_now*2<=100000 and position[N_now*2] == -1: #2배로 없앨 수 있는 거리를 +1로 없애는 거보다 먼저 처리를 해야 최소 거리를 유지할 수 있음.
        position[N_now*2] = position[N_now]
        q.appendleft(N_now*2)
    if 0<= N_now+1<=100000 and position[N_now+1] == -1:
        position[N_now+1] = position[N_now]+1
        q.append(N_now+1)

    

    
    
    
    