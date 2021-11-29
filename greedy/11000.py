from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
dic_room = defaultdict(int)
for _ in range(N):
    S, T = map(int, input().split())
    dic_room[S] +=1
    dic_room[T] -=1
print(sum(value for value in dic_room.values() if value>0))    
print(dic_room)