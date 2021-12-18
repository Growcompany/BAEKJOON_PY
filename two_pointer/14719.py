import sys

input = sys.stdin.readline

H, W = map(int,input().split())
arr = list(map(int,input().split()))

left_index = 0
left_max = arr[0]
right_index = W-1
right_max = arr[W-1]

result = 0

while left_index < right_index:
    if left_max<=right_max:
        left_index +=1
        left_max = max(left_max,arr[left_index])
        if left_max>arr[left_index]:
            result += left_max-arr[left_index]
    else:
        right_index -=1
        right_max = max(right_max,arr[right_index])
        if right_max>arr[right_index]:
            result += right_max-arr[right_index]
    
print(result)    