import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    arr = [0]+list(map(int,input().split()))
    team = []
    visited = [True]+[False for _ in range(n)]
    
    for i in range(1,n+1):
        if visited[i]:
            continue
        visited[i] = True
        
        q = [i]
        next_arr = arr[i]
        while True:
            if visited[next_arr]:
                if next_arr in q:
                    team += q[q.index(next_arr):]
                break
            else:
                q.append(next_arr)
                visited[next_arr] = True
                next_arr = arr[next_arr]
    
    print(n-len(team))