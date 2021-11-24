import sys
input = sys.stdin.readline

N = int(input())

line = list(map(int,input().split()))

line_sort = sorted(list(set(line)))

dic_line = dict() #아래 3줄을 {line_sort[i] : i for i in range(len(line_sort))} 이런 식으로도 가능 dictionary가 index보다 빠름 index는 느림
for i in range(len(line_sort)):
    dic_line[line_sort[i]] = i 

for i in range(len(line)):
    line[i] = dic_line[line[i]]
    
print(*line)