import random

file = open("input.txt", "w")

xVal = random.sample(range(1, 100), 2)
yVal = random.sample(range(1, 50), 2)

file.write(str(xVal[0]) + " " + str(yVal[0]) + "\n")
file.write(str(xVal[1]) + " " + str(yVal[1]) + "\n")
file.write("100 50\n")

for x in range(1, 101):
    for y in range(1, 51):
        if random.randint(0, 100) <= 10:
            file.write(str(x) + " " + str(y) + " 1\n")
        else:
            file.write(str(x) + " " + str(y) + " 0\n")
