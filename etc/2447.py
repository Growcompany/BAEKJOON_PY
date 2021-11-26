import sys

N = int(input())

star_type = [[]*(N) for _ in range(N)]
star_type[0] = '*'

k = 1

while True:
    if 3**k == N:
        break
    else:
        k+=1
        
def plus_star(num):
    for i in range(num//3):
        star_type[i+num//3] = star_type[i]+" "*(num//3)+star_type[i]
        star_type[i+(num//3)*2] = star_type[i]*3
        star_type[i] = star_type[i]*3
        
for i in range(1,k+1):
    i = 3**i
    plus_star(i)
    
for line in star_type:
    print(line)

    
    
    
#답
#N = int(input())

#stars = ["***", "* *", "***"]

#cnt = 0
#while N > 3:
#    N //= 3
#    cnt += 1


#def makeStar():
#    L = len(stars)
#    newStars = []
#    for i in range(L*3):
#    	# 빈칸을 만드는 규칙
#        if i // L == 1:
#            newStars.append(stars[i % L] + " " * L + stars[i % L])
#        else:
#            newStars.append(stars[i % L]*3)
#    return newStars


#for i in range(cnt):
#    stars = makeStar()

#for star in stars:
#    print(star)
    