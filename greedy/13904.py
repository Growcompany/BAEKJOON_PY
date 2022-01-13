import sys

input = sys.stdin.readline

N = int(input())
day = [0 for _ in range(1001)]
works = []
for _ in range(N):
    d, w = map(int,input().split())
    works.append((w,d))
    
works.sort(reverse = True)

result = 0

for w,d in works:
    for i in range(d-1,-1,-1):
        if day[i] == 0:
            day[i] = d
            result +=w
            break
            
print(result)