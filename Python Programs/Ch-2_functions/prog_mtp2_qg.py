#Program to implement random()
import random
#points = [20,40,10,30,15]; points = [30,50,20,40,45]
points = [30,50,20,40,45]
start = random.randint(1,3)
end = random.randint(2,4)
for c in range(start,end+1):
    print(points[c],"#",)
