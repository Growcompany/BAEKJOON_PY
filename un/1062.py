from collections import defaultdict
import sys

#풀이법을 2가지를 합친다고 하고 ㄱㄱ 1가지는 가장 적게 같이 나오는거 sort로 한거랑
#한개는 가장 적게 배워도 되는 문자
input = sys.stdin.readline

N, K = map(int,input().split())
dict_words = defaultdict(int)
words = []
result = 0

for _ in range(N):
    S += set(str(input().rstrip('\n')))
    words.append(S)
    for a in S:
        dict_words[a] +=1

sort_dict = sorted(dict_words.items(), key = lambda x:x[1], reverse = True)
words.sort()
if K<=len(sort_dict):
    sort_dict = dict(sort_dict[:K+3])

for S in words:
    temp = True
    for a in S:
        if not a in sort_dict.keys():
            temp = False
            break
    if temp:
        result +=1

print(words)
print(sort_dict)
print(result)