import sys

N = int(input())

star = [[]*(N+1) for _ in range()]

def basic_star(startx,endx):
    star[startx].append('111')
    star[startx+1].append('101')
    star[endx].append('111')
    
for i in range(1, N+1):
    basic_star()
    

    
    
    
#답
N = int(input())

stars = ["***", "* *", "***"]

cnt = 0
while N > 3:
    N //= 3
    cnt += 1


def makeStar():
    L = len(stars)
    newStars = []
    for i in range(L*3):
    	# 빈칸을 만드는 규칙
        if i // L == 1:
            newStars.append(stars[i % L] + " " * L + stars[i % L])
        else:
            newStars.append(stars[i % L]*3)
    return newStars


for i in range(cnt):
    stars = makeStar()

for star in stars:
    print(star)
    