import math
import sys
from classes.priorityQueue import minHeap
from classes.Vertex import Vertex
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from optimizedMemorySearchAlgos import isEdge



adjacents = {}
inputFile = sys.argv[1]

def read_input(inputFile):
    f = open(inputFile, "r")
    contents = f.readlines()
    start = tuple(map(int, contents[0].strip().split(" ")))
    end = tuple(map(int, contents[1].strip().split(" ")))
    size = list(map(int, contents[2].strip().split(" ")))
    vertices = {}
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
    
    for i in range(0,size[0]):
        for j in range(0,size[1]):
            if (data[j][i]==1):
                edge1 =(i+1,j+2)
                edge2 =(i+1,j+1)
                edge3 =(i+2,j+1)
                edge4 = (i+2,j+2)
                vertices[edge1] = []
                vertices[edge2] = []
                vertices[edge3] = []
                vertices[edge4] = []


    return start, end, size, data, visualizeData, vertices

def createAdjacencyList(start, end, size, data, vertices):
    vertices[start] = []
    vertices[end] = []
    for vertex in vertices:
        for vertex2 in vertices:
            if (vertex == vertex2):
                continue
            else:
                minX = min(vertex[0],vertex2[0])
                minY = min(vertex[1],vertex2[1])
                maxX = max(vertex[0],vertex2[0])
                maxY = max(vertex[1],vertex2[1])
                if (vertex[1]==vertex2[1]) and (minY + 1 <= size[1] + 1) and (minY-1 >= 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight((minX,minY + 1),(maxX,maxY),size,data,end) or lineOfSight((minX, minY - 1),(maxX,maxY),size,data,end))):
                        vertices[vertex].append(vertex2)
                    else:
                        continue
                elif (vertex[1]==vertex2[1]) and (maxY + 1 <= size[1] + 1) and (maxY-1 >= 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight((maxX,maxY + 1),(minX,minY),size,data,end) or lineOfSight((minX, minY - 1),(maxX,minY),size,data,end))):
                        vertices[vertex].append(vertex2)
                    else:
                        continue


                elif (vertex[0]==vertex2[0]) and (minX + 1 <= size[0] + 1) and (minX-1 >= 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight((minX+1,minY),(maxX,maxY),size,data,end) or lineOfSight((minX-1, minY),(maxX,maxY),size,data,end))):
                        vertices[vertex].append(vertex2)
                    else:
                        continue
                elif (vertex[0]==vertex2[0]) and (maxX + 1 <= size[0] + 1) and (maxX-1 >= 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight((maxX + 1,maxY),(minX,minY),size,data,end) or lineOfSight((maxX - 1, maxY),(minX,minY),size,data,end))):
                        vertices[vertex].append(vertex2)
                    else:
                        continue
                elif (vertex[0]==vertex2[0]) and (minX+1 <= size[0] + 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and lineOfSight((minX+1,minY),(maxX,maxY),size,data,end)):
                        vertices[vertex].append(vertex2)
                elif (vertex[0]==vertex2[0]) and (minX-1 >= 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and lineOfSight((minX-1, minY),(maxX,maxY),size,data,end)):
                        vertices[vertex].append(vertex)
                elif (vertex[0]==vertex2[0]) and (maxX+1 <= size[0] + 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and lineOfSight((maxX+1,maxY),(minX,minY),size,data,end)):
                        vertices[vertex].append(vertex2)
                elif (vertex[0]==vertex2[0]) and (maxX-1 >= 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and lineOfSight((maxX-1, maxY),(minX,minY),size,data,end)):
                        vertices[vertex].append(vertex2)

                elif (vertex2[1]==1) and (vertex[1]==1) and (vertex[0]<vertex2[1]) and ((vertex2[0],vertex2[1]+1) in vertices):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight(vertex,(vertex2[0],vertex2[1]+1),size,data,end))):
                        vertices[vertex].append(vertex2)
                elif (vertex2[1]==1) and(vertex[1]==1) and ((vertex[0],vertex[1]+1) in vertices):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight((vertex[0],vertex[1]+1),vertex2,size,data,end))):
                        vertices[vertex].append(vertex2)
                elif (vertex[1]==1) and (vertex2[1]==1) and (vertex[0]<vertex2[1]) and ((vertex2[0],vertex2[1]+1) in vertices):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight(vertex,(vertex2[0],vertex2[1]+1),size,data,end))):
                        vertices[vertex].append(vertex2)
                elif (vertex[1]==1) and (vertex2[1]==1) and((vertex[0],vertex[1]+1) in vertices):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight((vertex[0],vertex[1]+1),vertex2,size,data,end))):
                        vertices[vertex].append(vertex2)
                elif (vertex2[1]==size[1]+1) and (vertex[1]==size[1]+1) and (vertex[0]<vertex2[1]) and ((vertex2[0],vertex2[1]-1) in vertices):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight(vertex,(vertex2[0],vertex2[1]-1),size,data,end))):
                        vertices[vertex].append(vertex2)
                elif (vertex2[1]==size[1]+1) and (vertex[1]==size[1]+1) and ((vertex[0],vertex[1]-1) in vertices):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight((vertex[0],vertex[1]-1),vertex2,size,data,end))):
                        vertices[vertex].append(vertex2)
                elif (vertex[1]==size[1]+1) and (vertex2[1]==size[1]+1) and (vertex[0]<vertex2[1]) and ((vertex2[0],vertex2[1]-1) in vertices):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight(vertex,(vertex2[0],vertex2[1]-1),size,data,end))):
                        vertices[vertex].append(vertex2)
                elif (vertex[1]==size[1]+1) and (vertex2[1]==size[1]+1) and ((vertex[0],vertex[1]+1) in vertices):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight((vertex[0],vertex[1]-1),vertex2,size,data,end))):
                        vertices[vertex].append(vertex2)
                
                
                
                #vertical blocked cells at edges of grid
                elif (vertex2[0]==1) and (vertex[0]==1) and (vertex[1]>vertex2[0]) and ((vertex2[0]+1,vertex2[1]) in vertices):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight(vertex,(vertex2[0]+1,vertex2[1]),size,data,end))):
                        vertices[vertex].append(vertex2)
                        print(17)
                elif (vertex2[0]==1) and (vertex[0]==1) and ((vertex[0]+1,vertex[1]) in vertices):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight((vertex[0]+1,vertex[1]),vertex2,size,data,end))):
                        vertices[vertex].append(vertex2)
                        print(18)
                elif (vertex[0]==1) and (vertex2[0]==1) and (vertex[1]>vertex2[0]) and ((vertex2[0]+1,vertex2[1]) in vertices):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight(vertex,(vertex2[0]+1,vertex2[1]),size,data,end))):
                        vertices[vertex].append(vertex2)
                        print(19)
                elif (vertex[0]==1) and (vertex2[0]==1) and ((vertex[0]+1,vertex[1]) in vertices):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight((vertex[0]+1,vertex[1]),vertex2,size,data,end))):
                        vertices[vertex].append(vertex2)
                        print(20)
                elif (vertex2[0]==size[0]+1) and (vertex[0]==size[0]+1) and (vertex[1]<vertex2[0]) and ((vertex2[0]-1,vertex2[1]) in vertices):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight(vertex,(vertex2[0]-1,vertex2[1]),size,data,end))):
                        vertices[vertex].append(vertex2)
                        print(17)
                elif (vertex2[0]==size[0]+1) and (vertex[0]==size[0]+1) and ((vertex[0]-1,vertex[1]) in vertices):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight((vertex[0]-1,vertex[1]),vertex2,size,data,end))):
                        vertices[vertex].append(vertex2)
                elif (vertex[0]==size[0]+1) and (vertex2[0]==size[0]+1) and (vertex[1]<vertex2[0]) and ((vertex2[0]-1,vertex2[1]) in vertices):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight(vertex,(vertex2[0]-1,vertex2[1]),size,data,end))):
                        vertices[vertex].append(vertex2)
                elif (vertex[0]==size[0]+1) and (vertex2[0]==size[1]+1) and ((vertex[0]-1,vertex[1]) in vertices):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight((vertex[0]-1,vertex[1]),vertex2,size,data,end))):
                        vertices[vertex].append(vertex2)


                elif (vertex[1]==vertex2[1]) and (minY + 1 <= size[1] + 1) and (minY-1 >= 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight((minX,minY + 1),(maxX,maxY),size,data,end) or lineOfSight((minX, minY - 1),(maxX,maxY),size,data,end))):
                        vertices[vertex].append(vertex2)
                    else:
                        continue
                elif (vertex[1]==vertex2[1]) and (maxY + 1 <= size[1] + 1) and (maxY-1 >= 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight((maxX,maxY + 1),(minX,minY),size,data,end) or lineOfSight((minX, minY - 1),(maxX,minY),size,data,end))):
                        vertices[vertex].append(vertex2)
                    else:
                        continue
                elif (vertex[1]==vertex2[1]) and (minY+1 <= size[1] + 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and lineOfSight((minX,minY+1),(maxX,maxY),size,data,end)):
                        vertices[vertex].append(vertex2)
                elif (vertex[1]==vertex2[1]) and (minY-1 >= 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and lineOfSight((minX, minY - 1),(maxX,maxY),size,data,end)):
                        vertices[vertex].append(vertex)
                elif (vertex[1]==vertex2[1]) and (maxY+1 <= size[1] + 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and lineOfSight((maxX,maxY+1),(minX,minY),size,data,end)):
                        vertices[vertex].append(vertex2)
                elif (vertex[1]==vertex2[1]) and (maxY-1 >= 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and lineOfSight((maxX, maxY - 1),(minX,minY),size,data,end)):
                        vertices[vertex].append(vertex2)



                elif (vertex[0]==vertex2[0]) and (minX + 1 <= size[0] + 1) and (minX-1 >= 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight((minX+1,minY),(maxX,maxY),size,data,end) or lineOfSight((minX-1, minY),(maxX,maxY),size,data,end))):
                        vertices[vertex].append(vertex2)
                    else:
                        continue
                elif (vertex[0]==vertex2[0]) and (maxX + 1 <= size[0] + 1) and (maxX-1 >= 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and (lineOfSight((maxX + 1,maxY),(minX,minY),size,data,end) or lineOfSight((maxX - 1, maxY),(minX,minY),size,data,end))):
                        vertices[vertex].append(vertex2)
                    else:
                        continue
                elif (vertex[0]==vertex2[0]) and (minX+1 <= size[0] + 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and lineOfSight((minX+1,minY),(maxX,maxY),size,data,end)):
                        vertices[vertex].append(vertex2)
                elif (vertex[0]==vertex2[0]) and (minX-1 >= 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and lineOfSight((minX-1, minY),(maxX,maxY),size,data,end)):
                        vertices[vertex].append(vertex)
                elif (vertex[0]==vertex2[0]) and (maxX+1 <= size[0] + 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and lineOfSight((maxX+1,maxY),(minX,minY),size,data,end)):
                        vertices[vertex].append(vertex2)
                elif (vertex[0]==vertex2[0]) and (maxX-1 >= 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and lineOfSight((maxX-1, maxY),(minX,minY),size,data,end)):
                        vertices[vertex].append(vertex2)
                
                elif (vertex[1]==vertex2[1]) and (minY+1 <= size[1] + 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and lineOfSight((minX,minY+1),(maxX,maxY),size,data,end)):
                        vertices[vertex].append(vertex2)
                elif (vertex[1]==vertex2[1]) and (minY-1 >= 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and lineOfSight((minX, minY - 1),(maxX,maxY),size,data,end)):
                        vertices[vertex].append(vertex)
                elif (vertex[1]==vertex2[1]) and (maxY+1 <= size[1] + 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and lineOfSight((maxX,maxY+1),(minX,minY),size,data,end)):
                        vertices[vertex].append(vertex2)
                elif (vertex[1]==vertex2[1]) and (maxY-1 >= 1):
                    if (lineOfSight(vertex,vertex2,size,data,end) and lineOfSight((maxX, maxY - 1),(minX,minY),size,data,end)):
                        vertices[vertex].append(vertex2)



                else:
                    if lineOfSight(vertex,vertex2,size,data,end):
                        vertices[vertex].append(vertex2)
                

    return vertices

def algosMain(start,goal, data, size, adjacents, typeOfAlgo):
    sizeX = size[0]
    sizeY = size[1]
    startingVertex = Vertex(None, start)
    fringe = minHeap() 
    closedSet = set()

    startingVertex.setH(goal[0],goal[1])
    startingVertex.setF
    startingVertex.setParent(startingVertex)

    fringe.insert(startingVertex)
    while (fringe.notEmpty()):
        s = fringe.pop()
        #print(s.coords)
        if s.coords[0] == goal[0]:
            if s.coords[1] == goal[1]:
                return s
        #print(s.coords)
        #print("s coords")

        term = s.coords
        closedSet.add(term)
        #print(adjacents[term])
        print("Current Vertex: " + str(term) + ", H: " + str(s.h) + " , F:" + str(s.f) + " , G:" + str(s.g))
        for adjacentVertexCoords in adjacents[s.coords]:
            adjacentVertex = Vertex(None, (adjacentVertexCoords[0], adjacentVertexCoords[1]))
            adjacentTerm = (adjacentVertexCoords[0],adjacentVertexCoords[1])
            if not adjacentTerm in closedSet:
                #print(adjacentTerm)
                #print(adjacentVertex)
                #print (not fringe.contains(adjacentVertex))
                if not fringe.contains(adjacentVertex):
                    adjacentVertex.setG(math.inf)
                    adjacentVertex.setParent(None)
                    fringe = updateAStarVertex(s,adjacentVertex,fringe,data, size, goal)
                    

    return None


def lineOfSight(s,adjacentVertex,size, data, goal):
    sizeX = size[1]
    sizeY = size[0]
    x0 = s[1]
    y0 = s[0]
    x1 = adjacentVertex[1]
    y1 = adjacentVertex[0]
    f = 0
    dy = y1 - y0
    dx = x1 - x0
    if dy < 0:
        dy = -dy
        sY = -1
    else:
        sY = 1
    if (dx < 0):
        dx = -dx
        sX = -1
    else:
        sX = 1

    if (dx >= dy):
        while (x0 != x1):
            f = f + dy
            if (f >= dx):
                if data[x0+(sX-1)//2 - 1][y0 + (sY -1)//2 - 1]==1:
                    return False
                y0 = y0 + sY
                f = f - dx
            if (f!=0) and (data[x0+(sX-1)//2 -1][y0 + (sY -1)//2 - 1]==1):
                return False
            if (dy == 0) and (y0 < 0) and (y0 < sizeY) and (data[x0 + (sX - 1)//2 - 1][y0 -1]==1) and (data[x0 + (sX - 1)//2 - 1][y0 -2]==1):
                return False
            x0 = x0 + sX
    else:
        while (y0 != y1):
            f = f + dx
            if f >= dy:
                if data[x0 + (sX - 1)//2 - 1][y0 + (sY-1)//2 - 1]==1:
                    return False
                x0 = x0 + sX
                f = f - dy
            if (f!=0) and (data[x0 + (sX - 1)//2 - 1][y0 + (sY - 1)//2 - 1]==1):
                return False
            if (dx == 0) and (x0 < 0) and (x0 < sizeX) and (data[x0-1][y0 + (sY - 1)//2 - 1]==1 and (data[x0 - 2][y0 + (sY - 1)//2 -1])==1):
                return False
            y0 = y0 + sY
    return True

def updateThetaStarVertex(s, adjacentVertex, fringe, data, size, goal):
    if lineOfSight(s.parent,adjacentVertex, [size[0],size[1]], data, goal):
        if ((s.parent.g) + distanceFormula(s.parent, adjacentVertex)) < adjacentVertex.g:
            adjacentVertex.g = s.parent.g + distanceFormula(s.parent, adjacentVertex)
            adjacentVertex.setParent(s.parent)
            if fringe.contains(adjacentVertex):
                fringe.remove(adjacentVertex)
            adjacentVertex.setHtheta(goal[0], goal[1])
            adjacentVertex.setF()
            fringe.insert(adjacentVertex)
    return fringe


def updateAStarVertex(s, adjacentVertex, fringe, data, size, goal):
    distance = distanceFormula(s,adjacentVertex)
    if (s.g + distance < adjacentVertex.g):
        adjacentVertex.g = s.g + distance
        adjacentVertex.setParent(s)
        if fringe.contains(adjacentVertex):
            fringe.remove(adjacentVertex)
        adjacentVertex.setH(goal[0], goal[1])
        adjacentVertex.setF()
        print("Astar Adjacent Vertex: " + str(adjacentVertex.coords) + ", H: " + str(adjacentVertex.h) + " , F:" + str(adjacentVertex.f) + " , G:" + str(adjacentVertex.g))
        fringe.insert(adjacentVertex)
    return fringe


def distanceFormula(vertex, vertex2):
    return math.sqrt((vertex.coords[0]-vertex2.coords[0])**2 +  (vertex.coords[1]-vertex2.coords[1])**2)

def printGraph(vertices):
    for vertex in vertices:
        for vertex2 in vertices[vertex]:
            print("vertex: " + str(vertex) + " -> " + str(vertex2))


def main():
    start, end, size, data, visualizeData, vertices = read_input(inputFile)

    vertices = createAdjacencyList(start, end, size, data, vertices)

    goalVertex = algosMain(start, end, data, size, vertices, "aStar")
    
    title = "Visibility Graph with A* path algorithm"
    x, y = size[1], size[0]
    fig, ax = plt.subplots(1, 1, tight_layout=True)
    fig.suptitle(title, fontsize=20)
    my_cmap = matplotlib.colors.ListedColormap(['grey'])
    my_cmap.set_bad(color='w', alpha=0)
    for x in range(x+1):
        ax.axhline(x, lw=2, color='k', zorder=5)
    for y in range(y+1):
        ax.axvline(y, lw=2, color='k', zorder=5)

    ax.imshow(visualizeData, interpolation='none', cmap=my_cmap,
                extent=[0, y, 0, x], zorder=0)



    locs, labels = plt.xticks()
    labels = [int(item)+1 for item in locs]
    plt.xticks(locs, labels)

    locs, labels = plt.yticks()
    z = len(locs)
    labels = [z-int(item) for item in locs]
    plt.yticks(locs, labels)

    ax.xaxis.tick_top()
    ax.scatter(start[0]-1, x-start[1]+1, s=100,
                zorder=50, label="Start", clip_on=False)
    ax.scatter(end[0]-1, x-end[1]+1, s=100,
                zorder=50, label="Goal", clip_on=False)
    ax.legend()
    plt.axis('off')


    for vertex in vertices:
        for vertex2 in vertices[vertex]:
            # vertexCoordsStr = vertex.split(",")
            # vertexCoords = (int(vertexCoordsStr[0]),int(vertexCoordsStr[1]))
            x1 = vertex[0]
            y1 = vertex[1]
            x2 = vertex2[0]
            y2 = vertex2[1]
            plt.plot([x1-1, x2-1], [size[1]-y1+1, size[1]-y2+1],
                        zorder=50, color='green', linewidth=1.5, clip_on=False)
    
    current = goalVertex
    printGraph(vertices)
    print("Path from Goal to Start")
    print(str(size[0]) + " : " + str(size[1]))
    while (current.coords != start):
        currentParent = current.parent
        currentCoords = current.coords
        parentCoords = currentParent.coords
        x1 = currentCoords[0]
        y1 = currentCoords[1]
        x2 = parentCoords[0]
        y2 = parentCoords[1]
        print([x1,y1])


        a = plt.plot([x1-1, x2-1], [size[1]-y1+1, size[1]-y2+1],
                        zorder=50, color='red', linewidth=3, linestyle='dashed', clip_on=False)
        current = currentParent
    print(start)
    plt.savefig("visibilityGraph3.png")
    plt.show()

    return -1

if (__name__ == "__main__"):
    main()

