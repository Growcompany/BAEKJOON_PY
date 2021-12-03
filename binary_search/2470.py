import sys

input = sys.stdin.readline

N = int(input())
c = list(map(int,input().split()))
c.sort()

start = 0
end = N-1
result = abs(c[start]+c[end])

if c[-1]<0: #만약 음수 값만 있을 때
    print(c[-2],c[-1])
elif c[0] >0: #양수만 있을 때
    print(c[0],c[1])
else: #두 용액이 다 있을 때
    while start<end:
        temp = c[start] + c[end]
        if abs(temp)<abs(result):
            temp = c[start]+c[end]
            start = 
            if c[end] < 0:
                start +=1
            else:
                end -=1
            
        
        
        