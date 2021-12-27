N = int(input())

start = [2,3,5,7]
end = [1,3,7,9]

def find(num):
    for i in range(2,num**(0.5)+1):
        if num%i == 0:
            return
    if len(num) == N:
        return num
    
    for i in end:
        find(num+i)
        
for i in start:
    print(find(start))