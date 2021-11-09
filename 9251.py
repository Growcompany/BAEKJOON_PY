s = input()
s1 = input()

result = 0

for check in range(0,len(s)):
    checkpoint = 0
    temp = 0
    for i in range(check, len(s)):
        for j in range(checkpoint, len(s1)):
            if s[i] == s1[j]:
                checkpoint = j+1
                temp +=1
                break
    if temp > result:
        result = temp

print(result)
