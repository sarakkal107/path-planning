from cmath import nan
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math
import random


def read_input(inputFile):
    f = open(inputFile, "r")
    contents = f.readlines()
    start = tuple(map(int, contents[0].strip().split(" ")))
    end = tuple(map(int, contents[1].strip().split(" ")))
    size = list(map(int, contents[2].strip().split(" ")))

    visualizeData = np.full([size[1], size[0]], np.nan)
    data = [[0 for i in range(0, size[0])]  # 0s for x
            for j in range(0, size[1])]  # 0s for y
    i = 3

    while i < len(contents):
        temp = list(map(int, contents[i].split()))
        if (temp[2] == 1):
            visualizeData[temp[1]-1][temp[0]-1] = 1
            data[temp[1]-1][temp[0]-1] = 1
        i += 1
    return start, end, size, data, visualizeData

    # reads in the grid information

def generate_test(filePath):
    sizeX = 100
    sizeY = 50
    data, visualizeData = create_grid_with_blocks()
    startX = 0
    startY = -1
    goalX = 0
    goalY = 0
    validStart = False
    validGoal = False
    while not validStart:
        startX = random.randint(1,101)
        startY = random.randint(1,51)

        for count in range(4): #make sure that vertex isn't surrounded by 4 blocked cells
            if count == 0:
                adjacentX = startX
                adjacentY = startY + 1
            if count == 1:
                adjacentX = startX
                adjacentY = startY - 1
            elif count == 2:
                adjacentX = startX + 1
                adjacentY = startY
            elif count == 3:
                adjacentX = startX - 1
                adjacentY = startY
            if (adjacentX > 0 and adjacentY > 0) and (adjacentX <=  100 and adjacentY <= 50) and (data[adjacentY - 1][adjacentX - 1]==0):
                validStart = True
                break
    while not validGoal:
        goalX = random.randint(1,101)
        goalY = random.randint(1,51)

        for count in range(4): #make sure that vertex isn't surrounded by 4 blocked cells
            if count == 0:
                adjacentX = startX
                adjacentY = startY + 1
            if count == 1:
                adjacentX = startX
                adjacentY = startY - 1
            elif count == 2:
                adjacentX = startX + 1
                adjacentY = startY
            elif count == 3:
                adjacentX = startX - 1
                adjacentY = startY
            if (adjacentX > 0 and adjacentY > 0) and (adjacentX <=  100 and adjacentY <= 50) and (data[adjacentY - 1][adjacentX - 1])==0 and (startX != goalX or startY != goalY):
                validGoal = True
                break
    start = (startX,startY)
    goal = (goalX,goalY)
    size = [sizeX,sizeY]
    visualizeData = saveGrid(start,goal,size,data,visualizeData, filePath)
    return start,goal,size, data, visualizeData

def generate_grid(x, y, data, start, end):
    fig, ax = plt.subplots(1, 1, tight_layout=True)
    my_cmap = matplotlib.colors.ListedColormap(['grey'])
    my_cmap.set_bad(color='w', alpha=0)
    for x in range(x+1):
        ax.axhline(x, lw=2, color='k', zorder=5)
    for y in range(y+1):
        ax.axvline(y, lw=2, color='k', zorder=5)

    ax.imshow(data, interpolation='none', cmap=my_cmap,
              extent=[0, y, 0, x], zorder=0)

    plt.locator_params(axis="x", nbins=x+1)
    plt.locator_params(axis="y", nbins=y+1)

    locs, labels = plt.xticks()
    labels = [int(item)+1 for item in locs]
    plt.xticks(locs, labels)

    locs, labels = plt.yticks()
    z = len(locs)
    labels = [z-int(item) for item in locs]
    plt.yticks(locs, labels)

    ax.xaxis.tick_top()
    ax.scatter(start[0]-1, x-start[1]+1, s=50, zorder=50, label="Start")
    ax.scatter(end[0]-1, x-end[1]+1, s=50, zorder=50, label="End")
    ax.legend()
    plt.axis('off')
    plt.show()

def blocking():
    numIn100 = random.randint(1,100)
    blockValue = 0
    if numIn100 < 11:
        blockValue = 1
        return blockValue
    else:
        return blockValue

def create_grid_with_blocks():
    data = [[blocking() for i in range(100)] for j in range(50)]
    visualizeData = [[np.nan for i in range(100)] for j in range(50)]
    return data, visualizeData

def saveGrid(start,goal,size,data,visualizeData, filePath):
    file = open(filePath, "w")
    file.write(str(start[0])+ " " + str(start[1]))
    file.write("\n")
    file.write(str(goal[0])+ " " + str(goal[1]))
    file.write("\n")
    file.write(str(size[0]) + " " + str(size[1]))
    file.write("\n")
    for x in range (0,size[0]):
        for y in range(0,size[1]):
            if data[y][x] == 1:
                visualizeData[y][x] = 1
                blocked = 1
            else:
                blocked = 0
            file.write(str(x+1) + " " + str(y+1) + " " + str(blocked))
            file.write("\n")
    return visualizeData