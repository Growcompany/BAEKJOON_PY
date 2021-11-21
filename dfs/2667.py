import sys

input = sys.stdin.readline

N = int(input())

map_list = []

for i in range(N):
    line = list(map(int,str(input().rstrip('\n'))))
    map_list.append(line)

result = []
global count

def find_other(i,j):
    global count
    if i>0 and map_list[i-1][j] == 1: #위에꺼 체크
        map_list[i-1][j] = -1
        count +=1
        find_other(i-1,j)
    if i<N-1 and map_list[i+1][j] == 1: #아래꺼 체크
        map_list[i+1][j] = -1
        count +=1
        find_other(i+1,j)
    if j>0 and map_list[i][j-1] == 1: #왼쪽꺼 체크
        map_list[i][j-1] = -1
        count +=1
        find_other(i,j-1)
    if j<N-1 and map_list[i][j+1] == 1: #오른쪽꺼 체크
        map_list[i][j+1] = -1
        count +=1
        find_other(i,j+1)
    return
    
change = 0
for i in range(N):
    for j in range(N):
        count = 0
        if map_list[i][j] == 1:
            map_list[i][j] = -1
            find_other(i,j)  
            count +=1
            result.append(count)

print(len(result))
result.sort()
for num in result:
    print(num)

