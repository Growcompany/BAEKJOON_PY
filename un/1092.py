import sys

input = sys.stdin.readline

N = int(input())
kranes = list(map(int,input().split()))
K = int(input())
things = list(map(int,input().split()))

kranes.sort(reverse = True)
things.sort(reverse = True)

result = 0

if kranes[0]<things[0]:
    result = -1
else:
    while things:
        for i in range(N):
            for j in range(len(things)):
                if kranes[i]>=things[j]:
                    del things[j]
                    break
        result +=1

print(result)