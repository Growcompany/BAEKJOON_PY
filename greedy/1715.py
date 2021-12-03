import heapq
import sys

input = sys.stdin.readline

N = int(input())

cards = []

for _ in range(N):
    number = int(input())
    heapq.heappush(cards,number)

result = 0

while len(cards)>1:
    small_num1 = heapq.heappop(cards)
    small_num2 = heapq.heappop(cards)
    result += small_num1+small_num2
    heapq.heappush(cards,small_num1+small_num2)

print(result)