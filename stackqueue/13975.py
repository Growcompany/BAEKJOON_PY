import heapq
import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    K = int(input())
    book = list(map(int,input().split()))
    result = 0
    heapq.heapify(book)
    while len(book)>1:
        num1 = heapq.heappop(book)
        num2 = heapq.heappop(book)
        result += num1+num2
        heapq.heappush(book,num1+num2)
    print(result)