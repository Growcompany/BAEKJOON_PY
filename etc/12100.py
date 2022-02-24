import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
block = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs():
    q
    for i in range(4): # i가 0:아래로 1:위로 2:오른쪽 3:왼쪽
        if i==0: #아래로 밀때 왼쪽하단부터 시작
            for i in range(N,0,-1):
        


4 2
8 4
16 8

1)오른쪽으로 가는 경우 # 즉, y값이 +1로 이동하는 경우
체크 시작점=오른쪽 상단

2)왼쪽으로 가는 경우
체크 시작점=왼쪽 상단

3)위로 가는 경우
왼쪽 상단

4)아래로 가는 경우
왼쪽 하단 -> 