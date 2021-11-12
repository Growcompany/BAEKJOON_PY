import random

distance =[[999] for _ in range(5)]

for _ in range(random.randrange(3,7)):
    distance[0].append(random.randrange(1,7))    
    distance[1].append(random.randrange(1,7)) 
print(distance)

distance[0].sort()

print(distance)