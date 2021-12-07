#아래 방법은 시간초과 뜸 2진수를 이용해서 풀어야댐.. 근데 그건 따로 공부를 해야봐야 할 듯..
import sys

input = sys.stdin.readline

N, K = map(int,input().split())

def cal():
    squared = 1
    up_number = 2
    while True:
        if up_number<=N:
            up_number *=2
            squared+=1
        else:
            break

    accu_num = 0
    count = 0

    for i in range(K):
        up_number //= 2
        accu_num+=up_number

    while accu_num > N:
        accu_num -=up_number
        up_number //=2
        accu_num+=up_number
    accu_num +=up_number
    print(accu_num-N)

if K>N:
    print(-1)
else:
    cal()
    

        