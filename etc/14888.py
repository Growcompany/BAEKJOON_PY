from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
plus, minus, multi, div = map(int,input().split())

result = []

def bfs():
    q = deque()
    temp = arr[0]
    step = 1
    q.append((plus,minus,multi,div,temp,step))
    while q:
        p,m,mu,d,t,s = q.pop()
        
        if s==N:
            result.append(t)
        
        if p>0:
            q.append((p-1,m,mu,d,t+arr[s],s+1))
            
        if m>0:
            q.append((p,m-1,mu,d,t-arr[s],s+1))
        
        if mu>0:
            q.append((p,m,mu-1,d,t*arr[s],s+1))
        
        if d>0:
            if t<0:
                q.append((p,m,mu,d-1,-(abs(t)//arr[s]),s+1))
            else:
                q.append((p,m,mu,d-1,t//arr[s],s+1))
                    
bfs()
print(max(result))
print(min(result))