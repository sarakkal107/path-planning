import math
from classes.priorityQueue import minHeap
from classes.Vertex import Vertex
from graphStructure import add_vertex
from graphStructure import add_edge_weight


def algosMain(start,goal, data, size, adjacents, typeOfAlgo):
    sizeX = size[0]
    sizeY = size[1]
    startingVertex = Vertex(None, start)
    goalVertex = Vertex(None,[goal[0],goal[1]])
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
        print(s.coords)
        print("s coords")
        add_vertex(s, adjacents)
        addAdjacents(s,data,size,adjacents)
        term = str([s.coords[0],s.coords[1]])
        closedSet.add(s)
        #print(adjacents[term])
        for adjacentVertexCoords in adjacents[term]:
            adjacentVertex = Vertex(None, [adjacentVertexCoords[0], adjacentVertexCoords[1]])
            adjacentTerm = str([adjacentVertexCoords[0],adjacentVertexCoords[1]])
            if not adjacentVertex in closedSet:
                #print(adjacentTerm)
                #print(adjacentVertex)
                #print (not fringe.contains(adjacentVertex))
                if not fringe.contains(adjacentVertex):
                    adjacentVertex.setG(math.inf)
                    adjacentVertex.setParent(None)
                #print("about to update Vertex")
                if (typeOfAlgo == "aStar"):
                    fringe = updateAStarVertex(s,adjacentVertex,fringe,data, size, goal)
                elif (typeOfAlgo == "thetaStar"):
                    fringe = updateThetaStarVertex(s,adjacentVertex,fringe,data, size, goal)
                #print("updated vertex")

    return None

def updateAStarVertex(s, adjacentVertex, fringe, data, size, goal):
    #print(adjacentVertex.coords)
    #print(adjacentVertex.g)
    distance = distanceFormula(s,adjacentVertex)
    if (s.g + distance < adjacentVertex.g):
        #print(adjacentVertex.coords)
        adjacentVertex.g = s.g + distance
        adjacentVertex.setParent(s)
        if fringe.contains(adjacentVertex):
            fringe.remove(adjacentVertex)
        
        adjacentVertex.setH(goal[0], goal[1])
        adjacentVertex.setF()
        fringe.insert(adjacentVertex)
    return fringe


def lineOfSight(s,adjacentVertex,data, size):
    sizeX = size[0]
    sizeY = size[1]
    x0 = s.coords[0]
    y0 = s.coords[1]
    x1 = adjacentVertex.coords[0]
    y1 = adjacentVertex.coords[1]
    f = 0
    dy = y1 - y0
    dx = x1 - x0
    if dy < 0:
        dy = -1 * dy
        sY = -1
    else:
        sY = 1
    if (dx < 0):
        dx = -1 * dx
        sX = -1
    else:
        sX = 1

    if (dx >= dy):
        while (x0 != x1):
            f = f + dy
            if (f >= dx):
                if (data[x0+(sX-1)//2 - 1][y0 + (sY -1)//2 - 1]==1):
                    return False
                y0 = y0 + sY
                f = f - dx
            if (f!=0) and (data[x0+(sX-1)//2 -1][y0 + (sY -1)//2 - 1]==1):
                return False
            if (dy == 0) and (y0<0) and (y0 < sizeY) and (data[x0 + (sX - 1)//2 - 1][y0 -1]==1) and (data[x0 + (sX - 1)//2 - 1][y0 -2]==1):
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
            if (dx == 0) and (x0<0) and (x0 < sizeX) and (data[x0-1][y0 + (sY - 1)//2 - 1]==1 and (data[x0 - 2][y0 + (sY - 1)//2 -1])==1):
                return False
            y0 = y0 + sY
    return True

def updateThetaStarVertex(s, adjacentVertex, fringe, data, size, goal):
    if lineOfSight(s.parent,adjacentVertex, [len(data[0]),len(data)], data, goal): #path 2
        if (s.parent.g) + distanceFormula(s.parent, adjacentVertex) < adjacentVertex.g:
            adjacentVertex.g = s.parent.g + distanceFormula(s.parent, adjacentVertex)
            adjacentVertex.setParent(s.parent)
            if fringe.contains(adjacentVertex):
                fringe.remove(adjacentVertex)
            adjacentVertex.setH(goal[0], goal[1])
            adjacentVertex.setF()
            fringe.insert(adjacentVertex)
    else: #path 1
        fringe = updateAStarVertex(s, adjacentVertex, fringe, data, size, goal)
    
    return fringe


def distanceFormula(vertex, vertex2):
    return math.sqrt(math.pow(vertex.coords[0]+vertex2.coords[0],2) +  math.pow(vertex.coords[1]+vertex2.coords[1],2))

def addEdges(curVertexX, curVertexY, nextVertexX, nextVertexY, data, size, graph):
    if not (0 < nextVertexX and 0 < nextVertexY and nextVertexX <= size[0] + 1 and nextVertexY <= size[1] + 1):
        return
    sizeX = size[0]
    sizeY = size[1]
    #curVertexX = curVertex[1]
    #curVertexY = curVertex[0]
    #nextVertexX = nextVertex[1]
    #nextVertexY = nextVertex[0]
    if (curVertexX == nextVertexX):
        if (nextVertexY < curVertexY):
            if (curVertexX < sizeX + 1 and data[nextVertexY-1][curVertexX-1]==0) or (0 < curVertexY and data[nextVertexY-1][curVertexX-2]==0):
                add_edge_weight(curVertexX, curVertexY, nextVertexX, nextVertexY, graph, 1)
        else:
            if (curVertexX < sizeX + 1 and data[curVertexY-1][curVertexX-1]==0) or (0 < curVertexY and data[curVertexY-1][curVertexX-2]==0):
                add_edge_weight(curVertexX, curVertexY, nextVertexX, nextVertexY, graph, 1)
    elif (curVertexY == nextVertexY):
        if (nextVertexX < curVertexX):
            if (curVertexY < sizeY + 1 and data[curVertexY-1][nextVertexX-1]==0) or (0 < curVertexY and data[curVertexY-2][nextVertexX-1]==0):
                add_edge_weight(curVertexX, curVertexY, nextVertexX, nextVertexY, graph, 1)
        else:
            if (curVertexY < sizeY + 1 and data[curVertexY-1][curVertexX-1]==0) or (0 < curVertexY and data[curVertexY-2][curVertexX-1]==0):
                add_edge_weight(curVertexX, curVertexY, nextVertexX, nextVertexY, graph, 1)
    else:
        if ((curVertexY < nextVertexY) and (curVertexX > nextVertexX) and data[curVertexY-1][nextVertexX-1]==0):
            add_edge_weight(curVertexX, curVertexY, nextVertexX, nextVertexY, graph, math.sqrt(2)) #lower left
        elif ((curVertexY < nextVertexY) and (curVertexX < nextVertexX) and data[curVertexY-1][curVertexX-1]==0):
            add_edge_weight(curVertexX, curVertexY, nextVertexX, nextVertexY, graph, math.sqrt(2)) #lower left
        elif ((curVertexY > nextVertexY) and (curVertexX > nextVertexX) and data[nextVertexY-1][nextVertexX-1]==0):
            add_edge_weight(curVertexX, curVertexY, nextVertexX, nextVertexY, graph, math.sqrt(2)) #upper left
        elif ((curVertexY > nextVertexY) and (curVertexX < nextVertexX) and data[nextVertexY-1][curVertexX-1]==0):
            add_edge_weight(curVertexX, curVertexY, nextVertexX, nextVertexY, graph, math.sqrt(2)) #upper right

def addAdjacents(vertex, data, size, adjacents):
    vertexX = vertex.coords[0]
    vertexY = vertex.coords[1]
    addEdges(vertexX, vertexY, vertexX+1, vertexY, data, size, adjacents)
    addEdges(vertexX, vertexY, vertexX-1, vertexY, data, size, adjacents)
    addEdges(vertexX, vertexY, vertexX+1, vertexY+1, data, size, adjacents)
    addEdges(vertexX, vertexY, vertexX-1, vertexY+1, data, size, adjacents)
    addEdges(vertexX, vertexY, vertexX, vertexY+1, data, size, adjacents)
    addEdges(vertexX, vertexY, vertexX, vertexY-1, data, size, adjacents)
    addEdges(vertexX, vertexY, vertexX-1, vertexY-1, data, size, adjacents)
    addEdges(vertexX, vertexY, vertexX+1, vertexY-1, data, size, adjacents)