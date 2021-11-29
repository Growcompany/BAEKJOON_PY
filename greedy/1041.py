import sys
from itertools import combinations
import copy

input = sys.stdin.readline

N = int(input())
numbers = list(map(int,input().split()))
numbers_ordered = copy.deepcopy(numbers)
for i in range(len(numbers)):
    numbers_ordered[i] = [numbers[i],i]
    
def cal(number):
    com_list = list(combinations(numbers_ordered,number))
    min_num = 1e9
    for com in com_list:
        if numbers_ordered[0] in com and numbers_ordered[5] in com:
            continue
        if numbers_ordered[1] in com and numbers_ordered[4] in com:
            continue
        if numbers_ordered[2] in com and numbers_ordered[3] in com:
            continue
        sum_com = 0
        for num in com:
            sum_com += num[0]
        min_num = min(min_num,sum_com)
    return min_num

def solution(N,dice):
    three = cal(3)
    two = cal(2)
    one = min(numbers)
    print(three*4+two*4*(N-2)+(N-1)*(two*4+one*4*(N-2))+one*((N-2)**2))
    return

if N==1:
    print(sum(numbers)-max(numbers))
else:
    solution(N,numbers)
          