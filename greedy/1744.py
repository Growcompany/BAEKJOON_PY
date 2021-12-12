from bisect import bisect_right
import sys

input = sys.stdin.readline

N = int(input())
nums= []

for _ in range(N):
    nums.append(int(input()))
    
nums.sort()
zero_index = bisect_right(nums,0)

minus_list = nums[:zero_index]
plus_list = nums[zero_index:]

minus_result = 0
plus_result = 0
if len(minus_list)%2 == 1:
    minus_result += minus_list[-1]

for i in range(0,len(minus_list),2):
    if len(minus_list)-2 < i:
        break
    minus_result+=minus_list[i]*minus_list[i+1]

plus_list.sort(reverse=True)
if len(plus_list)%2 == 1:
    plus_result += plus_list[-1]
    
for i in range(0,len(plus_list),2):
    if len(plus_list)-2 < i:
        break
    if plus_list[i] == 1 or plus_list[i+1] == 1:
        plus_result += plus_list[i]+plus_list[i+1]
    else:
        plus_result+=plus_list[i]*plus_list[i+1]
        
print(minus_result+plus_result)