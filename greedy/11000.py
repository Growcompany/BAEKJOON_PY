import heapq
import sys
input = sys.stdin.readline

N = int(input())
lecture = []

for _ in range(N):
    S, T = map(int, input().split())
    lecture.append((S,T))
    
lecture.sort(key = lambda x:x[0])

room = []
heapq.heappush(room,lecture[0][1])
for i in range(1,len(lecture)):
    if room[0] > lecture[i][0]:
        heapq.heappush(room,lecture[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room,lecture[i][1])

print(len(room))











#from collections import defaultdict
#import sys
#input = sys.stdin.readline

#N = int(input())
#dic_room = defaultdict(int)
#for _ in range(N):
#    S, T = map(int, input().split())
#    dic_room[S] +=1
#    dic_room[T] -=1
#print(sum(value for value in dic_room.values() if value>0))    
#print(dic_room)