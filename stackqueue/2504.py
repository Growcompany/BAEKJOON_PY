from collections import deque
import sys

input = sys.stdin.readline

S = str(input())

def cal():
    result = 0
    q1 = deque()
    q2 = deque()
    for i in range(len(S)-1):
        if S[i] == '(':      
            q1.append(S[i])
        elif S[i] == ')':
            if S[i-1] == '[' or not q1:
                return 0
            q1.pop()       
        elif S[i] == '[':
            q2.append(S[i])
        elif S[i] == ']':
            if S[i-1] == '(' or not q2:
                return 0
            q2.pop()
        if S[i] == '(' and S[i+1] == ')':
            result +=(3**len(q2))*(2**len(q1))
            continue
        elif S[i] == '[' and S[i+1] == ']':
            result +=(3**len(q2))*(2**len(q1))
            continue
            
    if q1 or q2:
        return 0
    
    return result

print(cal())