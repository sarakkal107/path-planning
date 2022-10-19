import math
from classes.priorityQueue import minHeap
from classes.Vertex import Vertex


def algosMain(start,goal, data, size, typeOfAlgo):
    sizeX = size[0]
    sizeY = size[1]
    startingVertex = Vertex(None, start)
    fringe = minHeap() 
    closedSet = set()
    if typeOfAlgo=="thetaStar":
        startingVertex.setHtheta(goal[0],goal[1])
    else:
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

        term = str([s.coords[0],s.coords[1]])
        closedSet.add(term)
        #print("Current Vertex: " + term + ", H: " + str(s.h) + " , F:" + str(s.f) + " , G:" + str(s.g))
        for count in range(8):
            sX = s.coords[0]
            sY = s.coords[1]
            if count == 0:
                adjacentX = sX + 1
                adjacentY = sY + 1
            elif count == 1:
                adjacentX = sX - 1
                adjacentY = sY - 1
            elif count == 2:
                adjacentX = sX + 1
                adjacentY = sY - 1
            elif count == 3:
                adjacentX = sX - 1
                adjacentY = sY + 1
            elif count == 4:
                adjacentX = sX 
                adjacentY = sY + 1
            elif count == 5:
                adjacentX = sX
                adjacentY = sY - 1
            elif count == 7:
                adjacentX = sX - 1
                adjacentY = sY
            elif count == 8:
                adjacentX = sX + 1
                adjacentY = sY
            if not isEdge(sX,sY,adjacentX,adjacentY,data,size):
                continue
            adjacentVertex = Vertex(None, (adjacentX, adjacentY))
            adjacentTerm = str([adjacentX,adjacentY])
            if not adjacentTerm in closedSet:
                if not fringe.contains(adjacentVertex):
                    adjacentVertex.setG(math.inf)
                    adjacentVertex.setParent(None)
                    if (typeOfAlgo == "aStar"):
                        fringe = updateAStarVertex(s,adjacentVertex,fringe,data, size, goal)
                    elif (typeOfAlgo == "thetaStar"):
                        fringe = updateThetaStarVertex(s,adjacentVertex,fringe,data, size, goal)
        

    return None

def updateAStarVertex(s, adjacentVertex, fringe, data, size, goal):
    distance = distanceFormula(s,adjacentVertex)
    if (s.g + distance < adjacentVertex.g):
        #print(adjacentVertex.coords)
        adjacentVertex.g = s.g + distance
        adjacentVertex.setParent(s)
        if fringe.contains(adjacentVertex):
            fringe.remove(adjacentVertex)
        
        adjacentVertex.setH(goal[0], goal[1])
        adjacentVertex.setF()
        #print("Astar Adjacent Vertex: " + str(adjacentVertex.coords) + ", H: " + str(adjacentVertex.h) + " , F:" + str(adjacentVertex.f) + " , G:" + str(adjacentVertex.g))
        fringe.insert(adjacentVertex)
    return fringe


def lineOfSight(s,adjacentVertex,size, data, goal):
    sizeX = size[0]
    sizeY = size[1]
    x0 = s.coords[1]
    y0 = s.coords[0]
    x1 = adjacentVertex.coords[1]
    y1 = adjacentVertex.coords[0]
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
            #print("Theta Star Adjacent Vertex: " + str(adjacentVertex.coords) + ", H: " + str(adjacentVertex.h) + " , F:" + str(adjacentVertex.f) + " , G:" + str(adjacentVertex.g))
            fringe.insert(adjacentVertex)

    else:
        fringe = updateAStarVertex(s, adjacentVertex, fringe, data, size, goal)
    
    return fringe


def distanceFormula(vertex, vertex2):
    return math.sqrt((vertex.coords[0]-vertex2.coords[0])**2 +  (vertex.coords[1]-vertex2.coords[1])**2)

def isEdge(curVertexX, curVertexY, nextVertexX, nextVertexY, data, size):
    if not (0 < nextVertexX and 0 < nextVertexY and nextVertexX <= size[0] + 1 and nextVertexY <= size[1] + 1):
        return False
    sizeX = size[0]
    sizeY = size[1]
    if (curVertexX == nextVertexX):
        if (nextVertexY < curVertexY):
            if (curVertexX < sizeX + 1 and data[nextVertexY-1][curVertexX-1]==0) or (0 < curVertexX - 1 and data[nextVertexY-1][curVertexX-2]==0):
                return True
        else:
            if (curVertexX < sizeX + 1 and data[curVertexY-1][curVertexX-1]==0) or (0 < curVertexX - 1 and data[curVertexY-1][curVertexX-2]==0):
                return True
    elif (curVertexY == nextVertexY):
        if (nextVertexX < curVertexX):
            if (curVertexY < sizeY + 1 and data[curVertexY-1][nextVertexX-1]==0) or (0 < curVertexY - 1 and data[curVertexY-2][nextVertexX-1]==0):
                return True
        else:
            if (curVertexY < sizeY + 1 and data[curVertexY-1][curVertexX-1]==0) or (0 < curVertexY - 1 and data[curVertexY-2][curVertexX-1]==0):
                return True
    else:
        if ((curVertexY < nextVertexY) and (curVertexX > nextVertexX) and data[curVertexY-1][nextVertexX-1]==0):
            return True
        elif ((curVertexY < nextVertexY) and (curVertexX < nextVertexX) and data[curVertexY-1][curVertexX-1]==0):
            return True
        elif ((curVertexY > nextVertexY) and (curVertexX > nextVertexX) and data[nextVertexY-1][nextVertexX-1]==0):
            return True
        elif ((curVertexY > nextVertexY) and (curVertexX < nextVertexX) and data[nextVertexY-1][curVertexX-1]==0):
            return True