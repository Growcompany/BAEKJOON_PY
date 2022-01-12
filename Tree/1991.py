import sys
from collections import defaultdict
from collections import deque

input=sys.stdin.readline

N = int(input().rstrip('\n'))
graph = defaultdict(str)
result = [[],[],[]]

for _ in range(N):
    line = list(input().rstrip('\n').split())
    graph[line[0]] = [line[1],line[2]]
    
#전위&후위 순회 
def prepostorder(start):
    result[0].append(start)
    for node in graph[start]:
        if node != '.':
            prepostorder(node)
            result[2].append(node)
    return

def inorder(node):
    if node != '.':
        inorder(graph[node][0])  # left
        result[1].append(node) 
        inorder(graph[node][1])

prepostorder('A')
inorder('A')
print(''.join(result[0]))
print(''.join(result[1]))
print(''.join(result[2])+'A')

#---------------
import sys
 
N = int(sys.stdin.readline().strip())
tree = {}
 
for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]
 
 
def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right
 
 
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right
 
 
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root
 
 
preorder('A')
print()
inorder('A')
print()
postorder('A')
