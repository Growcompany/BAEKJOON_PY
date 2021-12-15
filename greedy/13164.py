import heapq
import sys

input = sys.stdin.readline

n, k = map(int,input().split())
children = list(map(int,input().split()))

arr = []

for i in range(n-1):
    arr.append(children[i+1]-children[i])

arr.sort()

print(sum(arr[:n-k]))