import sys

input = sys.stdin.readline

N, K = map(int,input().split())

A_list = []
for _ in range(N):
    num = int(input())
    A_list.append(num)
    
A_list.sort()
start = 1 # 집과 집사이의 설치 최소 거리
end = A_list[-1] - A_list[0] #집과 집 사이 거리의 최대 거리

while start<=end:
    count = 1 #설치된 공유기 개수
    mid = (start+end) // 2 #공유기 설치하는 거리를 이분탐색으로 찾아내기 위해서 반반 잘라서 계속 검색
    current = A_list[0] #처음부터 공유기 설치된 개수 체크용으로 공유기가 최신에 설치된 집 위치
    
    for i in range(1,N):
        if A_list[i] >= mid+current:
            count +=1
            current = A_list[i]
    
    if count >= K: #만약 거리를 너무 좁게해서 설치를 많이했다면? 거리를 좀 더 넓혀야지
        start = mid+1
        result = mid
    else:
        end = mid-1

print(result)

        
            
    