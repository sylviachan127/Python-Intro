#Yuen Han(Sylvia) Chan
#Section: B01
#GTID: #902983019
#Email: ychan35@gatech.edu
#I work on the entire HW by myself

import time
from math import*
import random
from Myro import*
import os
init()

def avgObstacleValues(n):
    import random
    import time
    ranN = random.uniform(0,1)
    timeC = 0
    leftValues = []
    centerValues = []
    rightValues = []
    for t in timer(n):
        leftValues.append(getObstacle("left"))
        centerValues.append(getObstacle("center"))
        rightValues.append(getObstacle("right"))
        turnLeft(1,ranN)
        timeC += 1
        print("1")

    newL = reduce((lambda x,y: x+y), leftValues)/timeC
    newC = reduce((lambda x,y: x+y), centerValues)/timeC
    newR = reduce((lambda x,y: x+y), rightValues)/timeC
    return(newL,newC,newR)

def findDistances(inF,outF):
    inFile = open(inF,"r")
    inFileA = []
    while True:
        theline = inFile.readline()
        if len(theline) == 0:
            break
        gg = theline.split()
        inFileA.append(gg)
    inFile.close()
    outFile = open(outF,"w")
    a= map((lambda item: sqrt((int(item[0])-int(item[2]))**2+(int(item[1])-int(item[3]))**2)),inFileA)
    for item in a:
        outFile.write(str(item)+"\n")
    outFile.close()

def findImages(site):
    myF = os.listdir(site)
    picNames = ["GIF","BMP","JPG","PNG","gif","bmp","jpg","gif"]
    myPics = []
    for item in myF:
        itemSplit = item.split(".")
        if itemSplit[len(itemSplit)-1] in picNames:
            myPics.append(item)
    print(myPics)

def generateFileSystemDictionary(path):
    dic = {}
    i = 0
    files=os.listdir(path)
    dic[path]=files
    while i == 0:
        for j in os.listdir(path):
            if os.path.isdir(path+os.sep+j) == True:
                path = path+os.sep+j
                dic[path]=os.listdir(path)
                i=0
            else:
                i=2
    print(i,path)
    return dic
