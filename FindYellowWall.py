#Yuen Han Chan & William Anderson
#Section: B01
#GTID:  902983019 & 903013679
#Collaberation: Pair Programming, work together with Will Anderson

from Myro import*
init()

def findYellow():
    setPicSize("small")
    p = takePicture()
    whitePixel = 0
    blackPixel = 0
    ratio = 0
    for pix in getPixels(p):
        red = getRed(pix)
        blue = getBlue(pix)
        green = getGreen(pix)
        if red > 120 and blue < 120 and green > 90:
            setRed(pix,255)
            setGreen(pix,255)
            setBlue(pix,255)
            whitePixel+=1
        else:
           setRed(pix,0)
           setGreen(pix,0)
           setBlue(pix,0)
        blackPixel+=1
    ratio = whitePixel/blackPixel
    print(whitePixel,blackPixel,ratio)
    show(p)
    return ratio

def musicScale():
    i = 0
    A = 880.000
    B = 987.767
    C = 523.251
    D = 587.330
    E = 659.255
    F = 698.456
    G = 783.991
    g=[C,F,E,F,C,0,C,F,E,F,C,0,C,F,E,F,F,F,D,D,C,0,C,F,E,F,C,0,C,A,G,G,F,0,C,F,E,D,0,D,D,F,F,D,C,0,D,D,F,F,E,E,0,A,A,E,G,F,F,E,F,0,F,E,F,B,C,C,B,A,G,0,D,D,F,F,E,E]
    while i<len(g):
        beep(.5,g[i])
        i=i+1



if getObstacle(1) < 6400:
    mypic = findYellow()
else:
    backward(1,1)
    mypic = findYellow()

while mypic <0.15:
    rotate(1,.5)
    mypic = findYellow()

while getObstacle(1) < 6400:
    forward(1, 1)
else:
    stop()

turnLeft(1,1)

musicScale()