from collections import deque
import sys
queue = deque('')

input = sys.stdin.readline

N = int(input())

def push_back(number):
    queue.append(number)

def push_front(number):
    queue.appendleft(number)

def front():
    if len(queue) < 1:
        print(-1)
    else:
        print(queue[0])
        
def back():
    if len(queue) < 1:
        print(-1)
    else:
        print(queue[-1])
        
def size():
    print(len(queue))

def empty():
    if len(queue) < 1:
        print(1)
    else:
        print(0)

def pop_front():
    if len(queue) < 1:
        print(-1)
    else:
        print(queue.popleft())

def pop_back():
    if len(queue) < 1:
        print(-1)
    else:
        print(queue.pop())

for _ in range(N):
    input_line = list(map(str,input().split()))
    if input_line[0] == 'push_back':
        push_back(input_line[1])
    elif input_line[0] == 'push_front':
        push_front(input_line[1])
    elif input_line[0] == 'front':
        front()
    elif input_line[0] == 'back':
        back()
    elif input_line[0] == 'size':
        size()
    elif input_line[0] == 'empty':
        empty()
    elif input_line[0] == 'pop_front':
        pop_front()
    elif input_line[0] == 'pop_back':
        pop_back()