import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math
import random


def read_input(inputFile):
    f = open(inputFile, "r")
    contents = f.readlines()
    start = list(map(int, contents[0].strip().split(" ")))
    end = list(map(int, contents[1].strip().split(" ")))
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
    #generate_grid(size[1], size[0], visualizeData, start, end)
    return start, end, size, data, visualizeData

    # reads in the grid information

def generate_test(filePath):
    sizeX = 100
    sizeY = 50
    data = create_grid_with_blocks()
    startX = 0
    startY = 0
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
            if (adjacentX > 0 and adjacentY > 0) and (adjacentX <=  100 and adjacentY <= 50) and (data[adjacentY - 1][adjacentX - 1]):
                validStart = True
                break
    while not validGoal:
        goalX = random.randint(1,101)
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
            if (adjacentX > 0 and adjacentY > 0) and (adjacentX <=  100 and adjacentY <= 50) and (data[adjacentY - 1][adjacentX - 1]) and (startX != goalX or startY != goalY):
                validGoal = True
                break
    start = [startX,startY]
    goal = [goalX,goalY]
    size = [sizeX,sizeY]
    saveGrid(start,goal,size,data,filePath)
    return start,goal,size, data, data

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
    if numIn100 < 11:
        return 1
    else:
        return 0

def create_grid_with_blocks():
    grid = [[blocking() for i in range(100)] for j in range(50)]
    return grid

def saveGrid(start,goal,size,data,filePath):
    file = open(filePath, "w")
    file.write(str(start[0])+ " " + str(start[1]))
    file.write("\n")
    file.write(str(goal[0])+ " " + str(goal[1]))
    file.write("\n")
    file.write(str(size[0]) + " " + str(size[1]))
    file.write("\n")
    for x in range (1,size[0]+1):
        for y in range(1,size[1]+1):
            if data[y - 1][x - 1] == 1:
                blocked = 1
            else:
                blocked = 0
            file.write(str(x) + " " + str(y) + " " + str(blocked))
            file.write("\n")