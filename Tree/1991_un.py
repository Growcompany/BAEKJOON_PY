import sys

input = sys.stdin.readline

N = int(input())

tree = []

for _ in range(N):
    root, left, right = map(int,input().split())
    