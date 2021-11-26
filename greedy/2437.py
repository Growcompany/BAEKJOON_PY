import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))
weights = list(map(int,input().rstrip('\n').split()))
weights.sort()
result = 0

for num in weights:
    if num>result+1:
        break
    else:
        result +=num
print(result+1)