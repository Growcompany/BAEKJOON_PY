import sys

input = sys.stdin.readline

T = int(input().rstrip('\n'))

for _ in range(T):
    N = int(input().rstrip('\n'))
    S = [input().rstrip('\n') for _ in range(N)]
    S.sort()
    result = True
    for i in range(N-1):
        if S[i] == S[i+1][:len(S[i])]:
            print('NO')
            result = False
            break
    
    if result:
        print('YES')
        
    
    