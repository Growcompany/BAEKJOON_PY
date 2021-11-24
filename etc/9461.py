T = int(input())

result = [1,1,1,2,2,3,4,5,7]

def triangle(num):
    if len(result)<num:
        for i in range(len(result),num):
            append_num = result[i-2]+result[i-3]
            result.append(append_num)
    print(result[num-1])

for _ in range(T):
    N = int(input())
    triangle(N)