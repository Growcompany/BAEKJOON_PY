import sys

input = sys.stdin.readline

S = list(str(input().rstrip('\n')))
S_stack = []

for i in range(len(S)):
    S_stack.append(S[i])
    if ''.join(S_stack[-4:]) == 'PPAP':
        for _ in range(3):
            S_stack.pop()
result = ''.join(S_stack)
if result == 'P' or result == 'PPAP':
    print('PPAP')
else:
    print('NP')