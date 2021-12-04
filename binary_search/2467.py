import sys

input = sys.stdin.readline

N = int(input())
c = list(map(int,input().split()))
c.sort()

start = 0
end = N-1
last_result = c[start]+c[end]
last_result_a = start
last_result_b = end

while start<end:
    temp = c[start] + c[end]
    if abs(temp) < abs(last_result):
        last_result = temp
        last_result_a = start
        last_result_b = end
        if temp == 0:
            break
    if temp<0:
        start +=1
    elif temp>0:
        end -= 1
        
print(c[last_result_a],c[last_result_b])

            
            
            
        
        
        