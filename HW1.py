#Yuen Han(Sylvia) Chan
#Section: B01
#GTID: #902983019
#Email: ychan35@gatech.edu
#I work on the entire HW by myself

#Convert Celsius to Fahrenheit
def celsiusToFahrenheit():
    celsius = input("Please enter the temperature in Celsius")
    celsiusFt = float(celsius)
    fahrenheit = float(9*(celsiusFt/5)+32)
    print(celsiusFt, "degrees in cesius equal to" ,fahrenheit, "degrees in fahrenheit")


import math
# calculate the volume of a cylinder
def cylinderVolume():
    radius = input("Please enter the radius in inches")
    radiusFt = float(radius)
    height = input("Please enter the height in inches")
    heightFt = float(height)
    volume = float(math.pi*radiusFt**2*heightFt)
    print("Volume of the cylinder is", volume, "inches clubed")


# convert seconds to the equivalent number of weeks, days, hours, minutes, and seconds.
def timeCleanUp():
    seconds = input("Please enter the number of seconds")
    secondsInt = int(seconds)
    weeks = int(secondsInt/604800)
    weeksLeft = secondsInt%604800
    days = int(weeksLeft/86400)
    dayLeft = secondsInt%86400
    hour = int(dayLeft/3600)
    hourLeft = secondsInt%3600
    minutes = int(hourLeft/60)
    minutesLeft = secondsInt%60
    print(secondsInt,"seconds equal to",weeks,"weeks",days,"days",hour,"hours",minutes,"minutes and",minutesLeft,"seconds")


#This program calculates a person's RI, Rohrer Index
def rohrerIndex():
    pound = input("Please enter your weight in pounds")
    poundFt = float(pound)
    riHeight = input("Please enter your height in inches")
    riHeightFt = float(riHeight)
    riCalc = (poundFt/riHeightFt**3)*2768
    round = (riCalc,2)
    print("Your RI is",riCalc)



