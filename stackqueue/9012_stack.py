import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    list_input = list(input().rstrip('\n'))
    list_stack = []
    vps = True
    for type in list_input:
        if type == '(':
            list_stack.append('(')
        elif type == ')':
            if len(list_stack) < 1:
                vps = False
                break
            else:
                list_stack.pop()
    
    if len(list_stack)>0:
        vps = False
    if vps:
        print('YES')
    else:
        print('NO')