import sys

input = sys.stdin.readline

N, K = map(int,input().split())
order = list(map(int,input().split()))

result = 0

if N<K:
    plug = []

    for i in range(K):
        check = False
        if len(plug)<N:
            if not order[i] in plug:
                plug.append(order[i])
            check = True
            continue
        if order[i] in plug:
            #print("같은거라 패스")
            #print(plug)
            continue
        
        del_num_index = -1
        farthest_index = -1

        for j in range(N):
            if not plug[j] in order[i:]:
                #print("뒤에 없는 가장 하빠리라 제거, 제거숫자:",plug[j])
                plug[j] = order[i]
                #print(plug)
                result +=1
                check = True
                break
            else:
                if farthest_index<order[i:].index(plug[j]):
                    farthest_index =order[i:].index(plug[j])
                    del_num_index = j
        
        if check:
            continue
        else:
            #print("뒤에 있는 거중에 가장 멀리 있는거 제일 멀리 측정된 인덱스:",del_num_index,"제거숫자:",plug[del_num_index])
            plug[del_num_index] = order[i]
            #print(plug)
            result +=1
                    
print(result)

#반례
#3 11
#11 8 11 7 2 8 2 7 5 10 2
    