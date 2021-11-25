from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())

team = []
for _ in range(N):
    team.append(list(map(int,input().rstrip('\n').split())))

team_type = list(combinations([i for i in range(N)],N//2))

min_gap = 1e9
for i in range(len(team_type)//2):
    com = team_type[i]
    link_list = team_type[-i-1]
    start = 0
    link = 0
    for i in range(N//2):
        for j in com:
            start += team[com[i]][j]
    for i in range(N//2):
        for j in link_list:
            link += team[link_list[i]][j]
    min_gap = min(min_gap,abs(link-start))
    
print(min_gap)
        

    