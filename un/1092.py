import sys

input = sys.stdin.readline

N = int(input())
kranes = list(map(int,input().split()))
K = int(input())
things = list(map(int,input().split()))

kranes.sort(reverse = True)
things.sort(reverse = True)

result = 0
things_check = 0

if kranes[0]<things[0]:
    result = -1
else:
    while things_check<K:
        for i in range(N):
            for j in range(things_check,K):
                if kranes[i]>=things[j]:
                    things_check = j+1
                    break
        result +=1

print(result)