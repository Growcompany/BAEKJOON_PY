import sys

input = sys.stdin.readline

N, M = map(int,input().rstrip('\n').split())
books = list(map(int,input().rstrip('\n').split()))

plus_num = []
minus_num = []

for num in books:
    if num>0:
        plus_num.append(num)
    else:
        minus_num.append(num)
        
plus_num.sort(reverse = True)
minus_num.sort(reverse = False)

result = 0
if plus_num and minus_num:
    max_num = max(abs(minus_num[0]),plus_num[0])
elif not plus_num:
    max_num = abs(minus_num[0])
elif not minus_num:
    max_num = plus_num[0]
    
for i in range(0, len(plus_num), M):
    if not plus_num[i] == max_num:
        result += 2*plus_num[i]

for i in range(0, len(minus_num), M):
    if not -minus_num[i] == max_num:
        result += -2*minus_num[i]
zubulun86
result += max_num
print(result)
    