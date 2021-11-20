import sys

input = sys.stdin.readline

N, M = map(int,input().split())
robot_a, robot_b, robot_dir = map(int,input().split())

dir_list = [0,1,2,3] # 0은 북쪽 1은 동쪽 2는 남쪽 3은 서쪽

room = [[]*M for _ in range(N)] #방 배치 0-빈공간 1-벽 2-청소완료된 빈공간

result = 1

for i in range(N):
    list_input = list(map(int,input().split()))
    room[i] = list_input        

room[robot_a][robot_b] = 2

def position_check(a,b):
    if room[a][b] == 0:
        room[a][b] == 2
        result+=1

while True: 
    if room[robot_a-1][robot_b] == 0 or room[robot_a+1][robot_b] == 0 or room[robot_a][robot_b-1] == 0 or room[robot_a][robot_b+1] == 0:
        if robot_dir == 3: #왼쪽 방향이 남쪽일떄
            if room[robot_a+1][robot_b] == 0:
                room[robot_a+1][robot_b] = 2
                robot_a += 1
                result+=1
            robot_dir = 2
        elif robot_dir == 0: #왼쪽이 서쪽일떄
            if room[robot_a][robot_b-1] == 0:
                room[robot_a][robot_b-1] = 2
                robot_b -= 1
                result+=1
            robot_dir = 3
        elif robot_dir == 2: #왼쪽이 동쪽일떄
            if room[robot_a][robot_b+1] == 0:
                room[robot_a][robot_b+1] = 2
                robot_b += 1
                result+=1
            robot_dir = 1
        elif robot_dir == 1: #왼쪽이 서쪽일떄
            if room[robot_a-1][robot_b] == 0:
                room[robot_a-1][robot_b] = 2
                robot_a -= 1
                result+=1
            robot_dir = 0
    else:
        if robot_dir == 0:
            if room[robot_a+1][robot_b] ==1:
                break
            else:
                robot_a +=1
                position_check(robot_a,robot_b)
        elif robot_dir == 1:
            if room[robot_a][robot_b-1] ==1:
                break
            else:
                robot_b -=1
                position_check(robot_a,robot_b)
        elif robot_dir == 2:
            if room[robot_a-1][robot_b] ==1:
                break
            else:
                robot_a -=1
                position_check(robot_a,robot_b)
        elif robot_dir == 3:
            if room[robot_a][robot_b+1] ==1:
                break
            else:
                robot_b +=1
                position_check(robot_a,robot_b)

print(result)
            
        
    



