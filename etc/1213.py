from collections import Counter
import sys

input = sys.stdin.readline

words = list(str(input().rstrip('\n')))
words.sort()
count = Counter(words)

middle = []
left = []
result = True
for key,value in count.items():
    if value%2 == 1:
        if middle:
            result = False
            break
        middle += key
        left.append(key*((value-1)//2))
    else:
        left.append(key*(value//2))
    
if result:
    print(''.join(left)+''.join(middle)+''.join(reversed(left)))
else:
    print("I'm Sorry Hansoo")
    