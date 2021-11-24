import sys

input = sys.stdin.readline

S = list(input().rstrip('\n'))
T = list(input().rstrip('\n'))

while len(S) != len(T):
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()

if S==T:
    print(1)
else:
    print(0)
    