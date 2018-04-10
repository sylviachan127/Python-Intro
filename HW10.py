#Yuen Han(Sylvia) Chan
#Section: B01
#GTID: #902983019
#Email: ychan35@gatech.edu
#I work on the entire HW by myself

from Myro import*
import time
import math
init()
#This homework contains 2 functions, one is to calculates the G Force,
#another one is to control robot with color.

def gravitationalForce():
#This function calculates the graviational Force based on user input
    gravity = 0.0000000000667
    mass1 = input("Please enter the known mass of object1 in kg")
    mass1ft = float(mass1)
    mass2 = input("please enter the known mass of object2 in kg")
    mass2ft = float(mass2)
    distance = input("Please enter the distance separating the objects' centers")
    distanceft = float(distance)
    fGrav = ((gravity*mass1ft*mass2ft)/(distanceft**2))
    print("The force of gravitational attraction between object1 and object2 with a distace of {0:.1f} is {1:.3f} N".format(distanceft,fGrav))

def moveWithColor(n):
#This function controls the robot's movement according
    for t in timer(n):
        p = takePicture()
        g = analysisPic(p)
        if g == "red":
            forward(1,1)
        elif g == "blue":
            backward(1,1)
        elif g == "green":
            rotate(1,1)

def analysisPic(aPic):
#This function returns the color result of the Picture to the moveWithColor function.
    rC=0
    gC=0
    bC=0
    tC=0
    bPercentage=0
    gPercentage=0
    colorI = ""
    for i in getPixels(aPic):
        r = getRed(i)
        g = getGreen(i)
        b = getBlue(i)
        if 100<r<255 and 60<g<110 and 50<b<120:
            rC +=1
            tC +=1
        elif r>100 and 200<g<270 and 170<b<210:
            gC +=1
            tC +=1
        elif 40<r<80 and 70<g<100 and 110<b<140:
            bC +=1
            tC +=1
        else:
            tC +=1
    #These calculate the percentage of red, green, and blue pixels in the picture.
    rPercentage=rC/tC
    bPercentage=bC/tC
    gPercentage=gC/tC
    if rPercentage > 0.05:
        colorI = "red"
    elif bPercentage > 0.05:
        colorI = "blue"
    elif gPercentage > 0.05:
        colorI = "green"
    print(rPercentage,bPercentage,gPercentage,colorI)
    #This returns the color of the picture to the moveWithColor function
    return colorI






