import sys

input = sys.stdin.readline

N, M = map(int,input().split())

map_A = [list(map(int,str(input().rstrip('\n')))) for _ in range(N)]
map_B = [list(map(int,str(input().rstrip('\n')))) for _ in range(N)]

if N<3 or M<3:
    if map_A == map_B:
        print(0)
    else:
        print(-1)
else:
    count = 0
    result = True
    
    for i in range(N-2):
        for j in range(M-2):
            if map_A[i][j] != map_B[i][j]:
                count +=1
                for a in range(i,i+3):
                    for b in range(j,j+3):
                        if map_A[a][b] == 0:
                            map_A[a][b] = 1
                        else:
                            map_A[a][b] = 0
    if map_A == map_B:
        print(count)
    else:
        print(-1)