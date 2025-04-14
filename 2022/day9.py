import pathlib
import sys
import os
from dataclasses import dataclass
import numpy as np


filePath = './data/'

@dataclass
class SimPosision:
    head: bool = False
    tail: bool = False
    tailVisited: bool = False

    def __str__(self) -> str:
        if self.head: return 'H'
        if self.tail: return 'T'
        if self.tailVisited: return '#'
        return '.'

    def __repr__(self) -> str:
        if self.head: return 'H'
        if self.tail: return 'T'
        if self.tailVisited: return '#'
        return '.'

def checkHead(el):
    return el.head
def checkTail(el):
    return el.tail


vHead = np.vectorize(lambda el : el.head)
vTail = np.vectorize(lambda el : el.tail)
vTailVis = np.vectorize(lambda el : el.tailVisited)


@dataclass
class StringSim:
    grid: any

    def __init__(self, d):
        self.grid = np.array([[SimPosision() for i in range(d)] for i in range(d)])
        self.grid[d-1,0].head = True
        self.grid[d-1,0].tail = True
        self.grid[d-1,0].tailVisited = True
        

    def __str__(self) -> str:
        return str(self.grid)

    def countVisited(self):
        return len(np.where(vTailVis(self.grid) == True )[0])
    
    def moveRight(self, n):
        headLoc = np.where(vHead(self.grid) == True )
        tailLoc = np.where(vTail(self.grid) == True )
        iYH = headLoc[0][0]
        iXH = headLoc[1][0]

        iYT = tailLoc[0][0]
        iXT = tailLoc[1][0]

        for i in range(n):
            self.grid[iYH, iXH].head = False #Unset head
            iXH+=1
            
            self.grid[iYH, iXH].head = True# set head in next position over

            if iXH - iXT > 1: # Check Tail
                if iYH == iYT:
                    self.grid[iYT, iXT].tail = False
                    iXT+=1
                    self.grid[iYT, iXT].tail = True
                    self.grid[iYT, iXT].tailVisited = True

                else:
                    self.grid[iYT, iXT].tail = False
                    iXT = iXT + 1 if iXH > iXT else iXT - 1
                    iYT = iYT + 1 if iYH > iYT else iYT - 1 

                    self.grid[iYT, iXT].tail = True
                    self.grid[iYT, iXT].tailVisited = True

    def moveLeft(self, n):
        headLoc = np.where(vHead(self.grid) == True )
        tailLoc = np.where(vTail(self.grid) == True )
        iYH = headLoc[0][0]
        iXH = headLoc[1][0]

        iYT = tailLoc[0][0]
        iXT = tailLoc[1][0]

        for i in range(n):
            self.grid[iYH, iXH].head = False #Unset head
            iXH-=1
            
            self.grid[iYH, iXH].head = True# set head in next position over

            if abs(iXH - iXT) > 1: # Check Tail
                if iYH == iYT:
                    self.grid[iYT, iXT].tail = False
                    iXT-=1
                    self.grid[iYT, iXT].tail = True
                    self.grid[iYT, iXT].tailVisited = True

                else:
                    self.grid[iYT, iXT].tail = False
                    iXT = iXT + 1 if iXH > iXT else iXT - 1
                    iYT = iYT + 1 if iYH > iYT else iYT - 1 

                    self.grid[iYT, iXT].tail = True
                    self.grid[iYT, iXT].tailVisited = True

    def moveDown(self, n):
        headLoc = np.where(vHead(self.grid) == True )
        tailLoc = np.where(vTail(self.grid) == True )
        iYH = headLoc[0][0]
        iXH = headLoc[1][0]

        iYT = tailLoc[0][0]
        iXT = tailLoc[1][0]

        for i in range(n):
            self.grid[iYH, iXH].head = False #Unset head
            iYH+=1
            
            self.grid[iYH, iXH].head = True# set head in next position over

            if iYH - iYT > 1: # Check Tail
                if iXH == iXT:
                    self.grid[iYT, iXT].tail = False
                    iYT+=1
                    self.grid[iYT, iXT].tail = True
                    self.grid[iYT, iXT].tailVisited = True

                else:
                    self.grid[iYT, iXT].tail = False
                    iXT = iXT + 1 if iXH > iXT else iXT - 1
                    iYT = iYT + 1 if iYH > iYT else iYT - 1 

                    self.grid[iYT, iXT].tail = True
                    self.grid[iYT, iXT].tailVisited = True

    def moveUp(self, n):
        headLoc = np.where(vHead(self.grid) == True )
        tailLoc = np.where(vTail(self.grid) == True )
        iYH = headLoc[0][0]
        iXH = headLoc[1][0]

        iYT = tailLoc[0][0]
        iXT = tailLoc[1][0]

        for i in range(n):
            self.grid[iYH, iXH].head = False #Unset head
            iYH-=1
            
            self.grid[iYH, iXH].head = True# set head in next position over

            
            if abs(iYH - iYT) > 1: # Check Tail
                # print("IN CHECK TAIL")
                if iXH == iXT:
                    self.grid[iYT, iXT].tail = False
                    iYT-=1
                    self.grid[iYT, iXT].tail = True
                    self.grid[iYT, iXT].tailVisited = True

                else:
                    self.grid[iYT, iXT].tail = False
                    iXT = iXT + 1 if iXH > iXT else iXT - 1
                    iYT = iYT + 1 if iYH > iYT else iYT - 1 

                    self.grid[iYT, iXT].tail = True
                    self.grid[iYT, iXT].tailVisited = True


def day9_part1(puzzle_input,d):
    # sim = StringSim(d)
    # print(sim)
    maxR = 0
    maxL = 0
    maxU = 0
    maxD = 0
    
    for line in puzzle_input:
        if line.split()[0] == 'R': maxR += int(line.split()[1])
        if line.split()[0] == 'L': maxL -= int(line.split()[1])
        if line.split()[0] == 'U': maxU += int(line.split()[1])
        if line.split()[0] == 'D': maxD -= int(line.split()[1])
    maxSize = max(abs(maxR),abs(maxL),abs(maxD),abs(maxU),d)

    sim = StringSim(maxSize)
    for line in puzzle_input:
        if line.split()[0] == 'R': sim.moveRight(int(line.split()[1]))
        if line.split()[0] == 'L': sim.moveLeft(int(line.split()[1]))
        if line.split()[0] == 'U': sim.moveUp(int(line.split()[1]))
        if line.split()[0] == 'D': sim.moveDown(int(line.split()[1]))

    # print()

    # print(sim)
    # print(sim.countVisited())
    
    return sim.countVisited()


print(day9_part1(pathlib.Path(filePath + 'day9.txt').read_text().splitlines(), 5000))