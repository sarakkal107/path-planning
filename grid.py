import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math


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
        temp = list(map(int, contents[i].strip().split(" ")))
        if (temp[2] == 1):
            visualizeData[temp[1]-1][temp[0]-1] = 1
            data[temp[1]-1][temp[0]-1] = 1
        i += 1
    #generate_grid(size[1], size[0], visualizeData, start, end)
    return start, end, size, data, visualizeData

    # reads in the grid information


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

# def addEdges(curVertexX, curVertexY, nextVertexX, nextVertexY, data, size, graph):
#     if not (0 < nextVertexX and 0 < nextVertexY and nextVertexX <= size[0] + 1 and nextVertexY <= size[1] + 1):
#         return
#     sizeX = size[0]
#     sizeY = size[1]
#     #curVertexX = curVertex[1]
#     #curVertexY = curVertex[0]
#     #nextVertexX = nextVertex[1]
#     #nextVertexY = nextVertex[0]
#     if (curVertexX == nextVertexX):
#         if (nextVertexY < curVertexY):
#             if (curVertexX < sizeX + 1 and data[nextVertexY-1][curVertexX-1]==0) or (0 < curVertexY and data[nextVertexY-1][curVertexX-2]==0):
#                 add_edge_weight(curVertexX, curVertexY, nextVertexX, nextVertexY, graph, 1)
#         else:
#             if (curVertexX < sizeX + 1 and data[curVertexY-1][curVertexX-1]==0) or (0 < curVertexY and data[curVertexY-1][curVertexX-2]==0):
#                 add_edge_weight(curVertexX, curVertexY, nextVertexX, nextVertexY, graph, 1)
#     elif (curVertexY == nextVertexY):
#         if (nextVertexX < curVertexX):
#             if (curVertexY < sizeY + 1 and data[curVertexY-1][nextVertexX-1]==0) or (0 < curVertexY and data[curVertexY-2][nextVertexX-1]==0):
#                 add_edge_weight(curVertexX, curVertexY, nextVertexX, nextVertexY, graph, 1)
#         else:
#             if (curVertexY < sizeY + 1 and data[curVertexY-1][curVertexX-1]==0) or (0 < curVertexY and data[curVertexY-2][curVertexX-1]==0):
#                 add_edge_weight(curVertexX, curVertexY, nextVertexX, nextVertexY, graph, 1)
#     else:
#         if ((curVertexY < nextVertexY) and (curVertexX > nextVertexX) and data[curVertexY-1][nextVertexX-1]==0):
#             add_edge_weight(curVertexX, curVertexY, nextVertexX, nextVertexY, graph, math.sqrt(2)) #lower left
#         elif ((curVertexY < nextVertexY) and (curVertexX < nextVertexX) and data[curVertexY-1][curVertexX-1]==0):
#             add_edge_weight(curVertexX, curVertexY, nextVertexX, nextVertexY, graph, math.sqrt(2)) #lower left
#         elif ((curVertexY > nextVertexY) and (curVertexX > nextVertexX) and data[nextVertexY-1][nextVertexX-1]==0):
#             add_edge_weight(curVertexX, curVertexY, nextVertexX, nextVertexY, graph, math.sqrt(2)) #upper left
#         elif ((curVertexY > nextVertexY) and (curVertexX < nextVertexX) and data[nextVertexY-1][curVertexX-1]==0):
#             add_edge_weight(curVertexX, curVertexY, nextVertexX, nextVertexY, graph, math.sqrt(2)) #upper right

# def addAdjacents(vertex, data, size, adjacents):
#     vertexX = vertex.coords[0]
#     vertexY = vertex.coords[1]
#     addEdges(vertexX, vertexX+1, vertexY, data, size, adjacents)
#     addEdges(vertexX, vertexY, vertexX-1, vertexY, data, size, adjacents)
#     addEdges(vertexX, vertexY, vertexX+1, vertexY+1, data, size, adjacents)
#     addEdges(vertexX, vertexY, vertexX-1, vertexY+1, data, size, adjacents)
#     addEdges(vertexX, vertexY, vertexX, vertexY+1, data, size, adjacents)
#     addEdges(vertexX, vertexY, vertexX, vertexY-1, data, size, adjacents)
#     addEdges(vertexX, vertexY, vertexX-1, vertexY-1, data, size, adjacents)
#     addEdges(vertexX, vertexY, vertexX+1, vertexY-1, data, size, adjacents)
