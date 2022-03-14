import sys

input = sys.stdin.readline

class Node: #기본적인 트리 구조 클래스
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        self.parent = -1

N = int(input())

tree = {}
depth = 1
column_cnt = 1
level_min = [N for _ in range(N+1)]
level_max = [0 for _ in range(N+1)]

for i in range(1, N+1): #트리구조를 이제 N만큼 기본 세팅
    tree[i] = Node(i, -1, -1)

for _ in range(N): #노드 정보를 받아들이고 자식과 부모노드를 세팅
    data, left_node, right_node = map(int,input().split())
    tree[data].left_node = left_node #자식 왼쪽꺼 세팅
    tree[data].right_node = right_node #자식 오른쪽 세팅
    if left_node != -1: #만약 왼쪽 자식 노드가 존재한다면
        tree[left_node].parent = data #부모를 지금 노드로 세팅
    if right_node != -1:
        tree[right_node].parent = data

for i in range(1, N+1):
    if tree[i].parent == -1:
        root = i #부모가 없는 노드를 찾아서 그걸 루트노드로 설정

def inorder(node, lev):
    global column_cnt, depth
    depth = max(depth, lev) #가장 깊은 깊이가 얼마나 되나 저장하는 용도
    if node.left_node != -1:
        inorder(tree[node.left_node], lev+1) #한번씩 더 돌 수록 현재 노드의 레벨을 더해준다

    #왼쪽 돌고 지금 현재 카운트 값을 다 지정하는거니까 중위순회
    print(node.data)
    level_min[lev] = min(level_min[lev], column_cnt)
    level_max[lev] = max(level_max[lev], column_cnt)
    column_cnt += 1

    if node.right_node != -1:
        inorder(tree[node.right_node], lev+1)
        
inorder(tree[root], 1)