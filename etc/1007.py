import sys, itertools

input=sys.stdin.readline

t = int(input())

for _ in range(t):
    num = int(input())
    sum_x = 0
    sum_y = 0
    points = []
    
    for _ in range(num):
        x, y = map(int,input().split())
        points.append([x,y])
        sum_x += x
        sum_y += y
        
    max_num = sys.maxsize
    
    combi = list(itertools.combinations(points,int(num/2)))
    combi_len = int(len(combi)/2)
                 
    for point in combi[:combi_len]:
        point = list(point)
                
        sum_xx = 0
        sum_yy = 0
        
        for xx,yy in point:
            sum_xx += xx
            sum_yy += yy
                
        result_x = sum_x - sum_xx
        result_y = sum_y - sum_yy

        re = min(ret, math.sqrt((sum_xx - result_x) ** 2 + (sum_yy - result_y) ** 2))
    print(re)
            