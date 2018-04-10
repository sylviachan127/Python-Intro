#Yuen Han Chan & William Anderson
#Section: B01
#GTID:  902983019 & 903013679
#Collaberation: Pair Programming, work together with Will Anderson

from Myro import*
init("sims")
def roboScript(fileName):

    f=open(fileName,"r")

    speed=0
    time=0


    while True:
        go=f.readline()
        if len(go)==0:
            break



        else:
            com=str(go)[0:2]
            if com=="fw":


                speed=float(str(go)[3])
                time=float(str(go)[5: ])
                forward(speed,time)

            elif com=="tr":

                speed=float(str(go)[3])
                time=float(str(go)[5: ])
                turnRight(speed,time)
    
            elif com=="bw":

                speed=float(str(go)[3])
                time=float(str(go)[5: ])
                backward(speed,time)
    
            elif com=="bp":

                freq=float(str(go)[3:7])
                time=float(str(go)[8: ])
                beep(time,freq)

            elif com=="tl":

                speed=float(str(go)[3])
                time=float(str(go)[5: ])
                turnLeft(speed,time)



    f.close()

