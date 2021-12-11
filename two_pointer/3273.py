import sys

input = sys.stdin.readline

N = int(input())
list_num = list(map(int,input().split()))
X = int(input())

list_num.sort()

result = 0
start = 0
end = N-1

while start<end:
    if list_num[start]+list_num[end] >X:
        end -=1
    elif list_num[start]+list_num[end] <X:
        start +=1
    else:
        result +=1
        start +=1
        
print(result)