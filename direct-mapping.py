# Copyright 2020, Massimiliano Sartore
# Licensed under the MIT license;

class Line:
    def __init__(self, blockValues, block, tag, lineNumber):
        self.blockValues = blockValues
        self.block = block
        self.tag = tag
        self.lineNumber = lineNumber
    def print(self):
        print(f'{self.lineNumber} - {self.block}:{self.tag} ({min(self.blockValues)}-{max(self.blockValues)})')
    
def blockNCalculator(mAddress, nWords):
    return int(mAddress/nWords)
    
def tagNCalculator(nBlock, nLine):
    return int(nBlock/nLine)

def lineNCalculator(nBlock, nLine):
    return nBlock%nLine

def listToIntList(list):
    intList = []
    for i in list:
        intList.append(int(i))
    return intList

def populateCache(maxNumber):
    cache = []
    for item in range(maxNumber+1):
        cache.append(item)
    return cache

def mappingCacheLines(fullIntList, blockSize):
    totalLines = []
    tempList = []
    for item in fullIntList:
        tempList.append(item)
        if len(tempList) == blockSize:
            totalLines.append(tempList)
            tempList = []

    if len(tempList) > 0:
        for item in range(blockSize-len(tempList)):
            tempList.append(tempList[len(tempList)-1]+1)
        totalLines.append(tempList)

    return totalLines

maxNumber = -1
lines = []

listInput = input("Enter a list of numbers: ")
listInput = listInput.split(',')
blockSize = int(input("Enter the block size: "))
linesNumber = int(input("Enter the number of lines: "))

intList = listToIntList(listInput)

for i in intList:
    if i > maxNumber:
        maxNumber = i

fullIntList = populateCache(maxNumber)

totalLines = mappingCacheLines(fullIntList, blockSize)

print("We are going to enter the initial list of lines (You have to write the block number ->0:0)")
while len(lines) != linesNumber:
    blockNumber = int(input("Enter a block number: "))
    if blockNumber > len(intList):
        raise ValueError("The list is not inside of the numbers you entered")
    else:
        lines.append(Line(totalLines[blockNumber], blockNumber, tagNCalculator(blockNumber, linesNumber), len(lines)))

print("List of lines:")
for line in lines:
    line.print()

hits = 0
for num in intList:
    numInLine = 0
    for line in lines:
        if num in line.blockValues:
            numInLine += 1

    if numInLine == 0:
        print(f"-----------------\nMISS: {num}")
        blockNumber = blockNCalculator(num, blockSize)
        lineNumber = lineNCalculator(blockNumber, linesNumber)
        lines[lineNumber].blockValues = totalLines[blockNumber]
        lines[lineNumber].tag = tagNCalculator(blockNumber, linesNumber)
        lines[lineNumber].block = blockNumber
        lines[lineNumber].lineNumber = lineNumber
        
        for i in range(len(lines)):
            if i == lineNumber:
                lines[i].print()
            else:
                print("|               |")
    else:
        hits+=1

print("\nHit Rate: {0:.3f}".format(hits/len(intList)))
