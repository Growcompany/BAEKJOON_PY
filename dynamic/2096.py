import sys
import copy

input = sys.stdin.readline

N = int(input())
room = []
max_sum = []
min_sum = []

for i in range(N):
    nums = list(map(int,input().split()))
    
    if i == 0:
        max_sum = nums
        min_sum = nums
    else:
        temp = [0,0,0]
        temp[0] = max(max_sum[0]+nums[0],max_sum[1]+nums[0])
        temp[1] = max(max_sum[0]+nums[1],max_sum[1]+nums[1],max_sum[2]+nums[1])
        temp[2] = max(max_sum[1]+nums[2],max_sum[2]+nums[2])
        
        max_sum = temp.copy()
        
        temp = [0,0,0]
        temp[0] = min(min_sum[0]+nums[0],min_sum[1]+nums[0])
        temp[1] = min(min_sum[0]+nums[1],min_sum[1]+nums[1],min_sum[2]+nums[1])
        temp[2] = min(min_sum[1]+nums[2],min_sum[2]+nums[2])
        
        min_sum = temp.copy()
        
print(max(max_sum),min(min_sum))