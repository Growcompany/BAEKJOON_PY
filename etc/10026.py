import sys
import copy

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

picture = [[0] for _ in range(N+2)]

for i in range(1, N+1):
    list_color = list(input())
    picture[i] = [0] + list_color + [0]

result = [0, 0]
picture[0] = list(0 for i in range(N+2))
picture[N+1] = list(0 for i in range(N+2))

picture_2 = copy.deepcopy(picture)

def change_GtoR():
    for i in range(1, N+1):
        for j in range(1, N+1):
            if picture_2[i][j] == 'G':
                picture_2[i][j] = 'R'

def check_same(picture, color: str, x, y):
    if color == picture[x-1][y]:
        picture[x-1][y] = 0
        check_same(picture, color, x-1, y)
    if color == picture[x+1][y]:
        picture[x+1][y] = 0
        check_same(picture, color, x+1, y)
    if color == picture[x][y-1]:
        picture[x][y-1] = 0
        check_same(picture, color, x, y-1)
    if color == picture[x][y+1]:
        picture[x][y+1] = 0
        check_same(picture, color, x, y+1)

def check_start(picture, result_num):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if picture[i][j] == 0:
                continue
            check_same(picture, picture[i][j], i, j)
            picture[i][j] = 0
            result[result_num] += 1


change_GtoR()
check_start(picture, 0)
check_start(picture_2, 1)
print(result[0],result[1])
