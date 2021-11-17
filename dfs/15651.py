N, M = map(int, input().split())

list_number = []

def print_number():
    if len(list_number) == M:
        print(' '.join(list_number))
        return

    for i in range(1,N+1):
        list_number.append(str(i))
        print_number()
        list_number.pop()

print_number()
    
        