from bisect import bisect_left
import sys

input = sys.stdin.readline

N = int(input())
A_list = list(map(int,input().split()))

save_list = []
save_list.append(A_list[0])

for i in range(1,N):
    pos = bisect_left(save_list,A_list[i])
    if len(save_list) <= pos:
        save_list.append(A_list[i])
    else:
        save_list[pos] = A_list[i]

print(len(save_list))
        
#정확한 수열을 구해내지는 못하지만 이분탐색을 활용하여 빠른속도로 길이만 알아내는 대에는 유용하다.