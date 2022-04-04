import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
nums = [True]*4_000_001

nums[1] = False
for i in range(2,2001):
  if nums[i]:
    for j in range(i+i,4_000_001,i):
      nums[j] = False
      
result = 0 
sum = 0
sum_list = deque([])

for i in range(n,1,-1):
  if nums[i]:
    sum_list.append(i)
    sum += i
  if sum == n:
    result +=1
    sum -= sum_list.popleft()
    #print(sum_list)
  if sum > n:
    sum -= sum_list.popleft()
print(result) 
   