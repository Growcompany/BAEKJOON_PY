import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    K = int(input())
    book = list(map(int,input().split()))
    result = 0
    while len(book)>1:
        min_index = 0
        min_result = 1e9
        print(book)
        for i in range(0,len(book)-1):
            if min_result>book[i]+book[i+1]:
                min_index = i
                min_result = book[i]+book[i+1]
        result +=min_result
        book.insert(min_index,min_result)
        del book[min_index+1]
        del book[min_index+1]
    print(result)
        
        