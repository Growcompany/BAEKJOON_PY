import sys

input = sys.stdin.readline

N = int(input())
lecture = []
for _ in range(N):
    start, end = map(int,input().split())
    lecture.append((start,end))
    
lecture.sort(key = lambda x: (x[1],x[0]))

before_end = lecture[0][1]
result = 1
for i in range(1,N):
    if before_end <= lecture[i][0]:
        before_end = lecture[i][1]
        result +=1

print(result)
