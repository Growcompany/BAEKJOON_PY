import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    AC = list(input())
    list_size = int(input())
    if list_size == 0:
        AC_list = input()
        AC_list = []
    else:
        AC_list = list(map(int,((input().lstrip("[").rstrip("]\n")).split(','))))
    AC_pop = 0
    AC_popleft = 0
    check_R = False
    for type in AC:
        if type == 'R':
            if check_R:
                check_R = False
            else:
                check_R = True
        elif type == 'D':
            if check_R:
                AC_pop +=1
            else:
                AC_popleft +=1
    if len(AC_list)<(AC_popleft + AC_pop):
        print("error")
    else:
        for _ in range(AC_popleft):
            AC_list.pop(0)
        for _ in range(AC_pop):
            AC_list.pop()
        if check_R:
            AC_list.reverse()
        print('[', end = '') #진짜 문제 더럽게 낸다;;; ㄹㅇ 아니 이거가지고;;;
        for i,number in enumerate(AC_list):
            if i == len(AC_list)-1:
                print(number, end = '')
            else:
                print(number, end = ',')
        print(']')
            