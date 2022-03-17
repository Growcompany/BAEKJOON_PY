import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    visited = [False]*1_000_000 #숫자가 저장된건지 체크용
    max_heap = [] #pop을하면 가장 큰 수가 나오게
    min_heap = []
    for i in range(N):
        check, num = map(str,input().split())
        num = int(num)
        if check == 'I':
            heapq.heappush(max_heap,(-num,i)) #숫자랑 index용으로 i를 넣는데 i를 넣는 이유는 숫자 식별용으로 안겹치게 그니까 i가 숫자를 의미하는게 아니라 몇번쨰 숫자가 체크가 됬는지 ㅇㅇ
            heapq.heappush(min_heap,(num,i))
            visited[i] = True #이 숫자가 들어왔다고 체크
        else:
            if num == -1: #최솟값 삭제
                while min_heap and not visited[min_heap[0][1]]: #체크가 다시 풀린(그니까 max에서 지운) 숫자가 있으면 바로바로 제거 동기화작업
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False #삭제를 visited으로 체크를 풀어서 max에서도 동기화되게
                    heapq.heappop(min_heap)
            else:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]: #마지막으로 체크안된거 다 정리하기
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    if max_heap and min_heap:
        print(-max_heap[0][0],min_heap[0][0])
    else:
        print('EMPTY')
