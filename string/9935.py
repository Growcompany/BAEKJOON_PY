import sys

input = sys.stdin.readline

S = input().rstrip('\n')
bomb = input().rstrip('\n')
q = []

for a in S:
    q.append(a)
    if len(q) >= len(bomb):
        if ''.join(q[-len(bomb):]) == bomb:
            for _ in range(len(bomb)):
                q.pop()
                
if len(q) == 0:
    print('FRULA')
else:
    print(''.join(q))