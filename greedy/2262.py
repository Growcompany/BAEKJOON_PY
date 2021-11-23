import sys

input = sys.stdin.readline

n = int(input())
members = list(map(int,input().rstrip('\n').split()))

result = 0
while len(members) > 1:
    max_index = members.index(max(members))
    if max_index>0 and max_index<(len(members)-1):
        result += members[max_index] - max(members[max_index-1],members[max_index+1])
    elif max_index == 0:
        result += members[max_index] - members[max_index+1]
    elif max_index == len(members)-1:
        result += members[max_index] - members[max_index-1]
    del members[max_index]
print(result)
        
    