#Our own implementation of a min-heap to use as our priority queue. Our min heap would use th minimum f values of the vertices to order the heap.
import math
from classes.Vertex import Vertex

class minHeap:

    def __init__(self):
        self.size = 0
        self.heap = []

    def parentOfNum(self, num):
        return (num - 1) // 2 #In order to get parent, need the floor of the current number node in min-heap subtracted by 1 and divided by 2
    
    def leftChildOfNum(self,num):
        return 2 * num + 1

    def rightChildOfNum(self,num):
        return 2 * num + 2


    def minHeapify(self, num):
        if self.size < 2: 
            return


        leftNum = self.leftChildOfNum(num)
        rightNum = self.rightChildOfNum(num)
        smallestNum = num
        if leftNum < self.size and self.heap[leftNum].f < self.heap[smallestNum].f:
            smallestNum = leftNum
        if rightNum < self.size and self.heap[rightNum].f < self.heap[smallestNum].f:
            smallestNum = rightNum

        if smallestNum != num:
            self.switch(num, smallestNum)
            self.minHeapify(smallestNum)  

    def switch(self, num1, num2):
        temp = self.heap[num1]
        self.heap[num1] = self.heap[num2]
        self.heap[num2] = temp

    def contains(self, vertex):
        if (vertex in self.heap):
            return True
        else:
            return False

    def pop(self):
        minimum = self.heap[0]
        
        self.switch(0, self.size - 1)
        self.heap.pop(self.size - 1)
        self.size -= 1
        self.minHeapify(0)

        return minimum
    
    def insert(self, vertex):
        self.heap.append(vertex)
        self.size += 1
        num = self.size - 1 # index of newly added vertex
        currentF = vertex.f
        parentF = self.heap[self.parentOfNum(num)].f
        while num > 0 and (currentF < parentF):
            self.switch(num,self.parentOfNum(num))
            num = self.parentOfNum(num)
            parentF = self.heap[self.parentOfNum(num)].f
            currentF = self.heap[num].f

        
    def remove(self, vertex):
        num = self.heap.index(vertex)

        temp = Vertex(None, None)
        temp.setG(-math.inf)
        temp.setF()
        self.heap[num] = temp

        currentNum = num
        currentVertex = temp
        while currentNum > 0 and currentVertex.f < self.heap[self.parentOfNum(currentNum)].f:
            self.switch(currentNum, self.parentOfNum(currentNum))
            currentNum = self.parentOfNum(currentNum) 
            currentVertex = self.heap[self.parentOfNum(currentNum)]
            
        self.pop()
    
    def notEmpty(self):
        if (self.size > 0):
            return True
        else:
            return False






