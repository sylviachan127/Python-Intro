#Yuen Han Chan & William Anderson
#Section: B01
#GTID:  902983019 & 903013679
#Collaberation: Pair Programming, work together with Yuen Han CHan

from Myro import*
import time
init()

def seeingRed():
    p = takePicture()
    n = makePicture(p)
    for i in getPixels(n):
        setRed(i,244)

    show(n)

def fade():
    p = takePicture()
    gif = []
    n = makePicture(p)
    n2 = copyPicture(n)
    x=0
    show(n)
    while x<50:
        for i in getPixels(n):
            setRed(i,getRed(i)-x)
            setGreen(i,getGreen(i)-x)
            setBlue(i,getBlue(i)-x)
        f=copyPicture(n)
        gif.append(f)
        x=x+5

    savePicture(gif,"fade.gif")

def overLay():
    p = takePicture()
    n = makePicture(p)
    for x in range(40,70):
        for y in range(36,94):
            imagx = getPixel(n,x,y)
            setGreen(imagx, 255)
    for x in range(90,120):
        for y in range(36,94):
            imagx = getPixel(n,x,y)
            setGreen(imagx, 255)
    for x in range(55,105):
        for y in range(120,130):
            imagx = getPixel(n,x,y)
            setRed(imagx, 255)
        show(n)

#Assume both pictures are the same size
def greenScreen():
  a = takePicture()
  turnLeft(1,1)
  b = takePicture()
  green=makePicture(a)
  black=makePicture(b)
  for x in range(getWidth(green)):
     for y in range(getHeight(black)):
        gre=getPixel(green,x,y)
        bla=getPixel(black,x,y)
        g1=getGreen(gre)
        r2=getRed(bla)
        b2=getBlue(bla)
        g2=getGreen(bla)
        if g1 >130:
          setBlue(gre,b2)
          setRed(gre,r2)
          setGreen(gre,g2)
  show(green)

#Assume both pictures are the same size
def shake():
    gif = []
    n = takePicture()
    p = makePicture(n)
    turnLeft(1,1)
    n2 = takePicture()
    p2 = makePicture(n2)
    show(p); show(p2)
    for z in getPixels(p):
        setRed(z,0)
        setBlue(z,0)
        setGreen(z,0)
    j=0
    xx=0
    yy=0
    xList=[0,10,-5,10,-10,0,5,-20,0]
    hh = getHeight(p)
    ww = getWidth(p)
    while j<(len(xList)):
        for x in range(0,ww):
            for y in range(0,hh):
                yList=[0,20,-20,0,20,-20,0,20,-20]
                xx = xList[j]
                yy = yList[j]

                pix = getPixel(p,x-xx,y-yy)
                pix2 = getPixel(p2,x,y)
                setRed(pix,getRed(pix2))
                setGreen(pix,getGreen(pix2))
                setBlue(pix,getBlue(pix2))
        j=j+1
        show(p)
        f=copyPicture(p)
        gif.append(f)
    savePicture(gif,"shake.gif")

def colorSnow():
    #Allows the picture to have different color sprinkle
    #Me and my partner think this worth 30 points
    p = takePicture()
    n = makePicture(p)
    height = getHeight(n)
    width = getWidth(n)

    for x in range(0,width,40):
        for y in range(0,height, 40):
            imagz = getPixel(n,x,y)
            setRed(imagz,255)
    for x in range(10,width,40,):
        for y in range(10,height, 40):
            imagz = getPixel(n,x,y)
            setBlue(imagz,255)
    for x in range(20,width,40,):
        for y in range(20,height, 40):
            imagz = getPixel(n,x,y)
            setGreen(imagz,255)
    for x in range(30,width,40,):
        for y in range(30,height, 40):
            imagz = getPixel(n,x,y)
            setRed(imagz,255)
            setGreen(imagz,255)
            setBlue(imagz,255)
        show(n)
