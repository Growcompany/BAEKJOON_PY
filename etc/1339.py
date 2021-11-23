import sys

input = sys.stdin.readline

N = int(input().rstrip('\n'))

alphabet = set()
words = []
result =0
for _ in range(N):
    line = list(input().rstrip('\n'))
    words.append(line)
    alphabet.update(line)

dict_alphabet = dict()

for alpha in alphabet:
    dict_alphabet[alpha] = 0
    
for line in words:
    len_line = len(line)
    for i in range(len(line)):
        dict_alphabet[line[i]] = 10**(len_line-i-1)+dict_alphabet[line[i]]
        
list_alphabet = list(dict_alphabet.items())
list_alphabet.sort(key = lambda x:x[1],reverse = True)
for i in range(1,len(list_alphabet)+1):
    result +=list_alphabet[i-1][1]*(10-i)
    
print(result)