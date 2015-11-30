#Author: Frank Dong
#Date: Oct 24, 2015
#Purpose: To create a program which will simulate the output of pollutant flowing
#        between ponds

#Import Graphics Package
from plotpoints import *

#Set flow rate constant as 0.005
FLOW_RATE = 0.005

#Purpose: To calculate the amount of pollutant in pond one
#Parameter: pond1Flow, pond3Flow, leakRate
#Return: Calculated pond one pollutant
def pondOnePollutant (pond1Flow, pond3Flow, leakRate):
    return pond1Flow + (pond3Flow * FLOW_RATE) - (pond1Flow * FLOW_RATE) + leakRate

#Purpose: To calculate the amount of pollutant in pond two
#Parameter: pond1Flow, pond2Flow
#Return: Calculated pond two pollutant
def pondTwoPollutant (pond1Flow, pond2Flow):
    return pond2Flow + (pond1Flow * FLOW_RATE) - (pond2Flow * FLOW_RATE)

#Purpose: To calculate the amount of pollutant in pond three
#Parameter: Pond2Flow, pond3Flow
#Return: calculated pond three pollutant
def pondThreePollutant (pond2Flow, pond3Flow):
    return pond3Flow + (pond2Flow * FLOW_RATE) - (pond3Flow * FLOW_RATE)

#=========================== Main ============================
pondOne = []
pondTwo = []
pondThree = []

#Input Statements
maxLeakAmount = input ("Please enter the maximum amount of pollutant: ")
while maxLeakAmount.isalpha():
    maxLeakAmount = input ("INVALID! Please enter a valid NUMERIC maximum amount of pollutant: ")
while float(maxLeakAmount) < 0:
    maxLeakAmount = input ("INVALID! Please enter a valid POSITIVE maximum amount of pollutant: ")
    
time = input ("Please enter the time you wish to run this simulation for: ")
while time.isalpha():
    time = input ("INVALID! Please enter a valid NUMERIC time you wish to run this simulation for: ")
while float(time) < 0:
    time = input ("INVALID! Please enter a valid POSITIVE time you wish to run this simulation for: ")
    
leakRate = input ("Please enter the leak rate: ")
while leakRate.isalpha():
    leakRate = input ("INVALID! Please enter a valid NUMERIC leak rate: ")
while float(leakRate) < 0:
    leakRate = input ("INVALID! Please enter a valid POSITIVE leak rate: ")

#Conversion on inputted values 
maxLeakAmount = float(maxLeakAmount)
time = float(time)
leakRate = float(leakRate)
leakAmount = 0

#Adding first value onto list (at minute = 0)
pondOne.append(0)
pondTwo.append(0)
pondThree.append(0)

#Loop appending pollutant value onto lists for x amount of time
for count in range (int(time)):
    if (leakAmount >= int(maxLeakAmount)):
        leakRate = 0
    pondOne.append(pondOnePollutant(pondOne[count], pondThree[count], leakRate))
    pondTwo.append(pondTwoPollutant(pondOne[count], pondTwo[count]))
    pondThree.append(pondThreePollutant(pondTwo[count], pondThree[count]))
    leakAmount = leakAmount + leakRate

#Print statements
count = 0
while (count < time):
    if (count % 60) == 0:
        print ("=" * 50)
        print ("Level of Pollutant at:",count,"Minute(s)")
        print ("Pond One:", (pondOne[count]), "L")
        print ("Pond Two:", (pondTwo[count]), "L")
        print ("Pond Three:", (pondThree[count]), "L")
    count = count + 1
print ("=" * 50)
print ("Final Level of Pollutant at:",count,"Minutes(s)")
print ("Pond One:", (pondOne[count]))
print ("Pond Two:", (pondTwo[count]))
print ("Pond Three:", (pondThree[count]))
print ("=" * 21, "Legend", "=" * 21)
print ("Red - Indicates Pond 1 pollution")
print ("Blue - Indicates Pond 2 pollution")
print ("Green - Indicates Pond 3 pollution")

#GRAPHICS
win = GraphicsWindow(500, 500)
canvas = win.canvas()

## Creates a grid with x being the time and y being the maxLeakAmount
createGrid(canvas,int(time),int(maxLeakAmount))

## Draw three lines of pond one, two and three
for t in range (int(time)):
    drawDots(canvas,t,time,pondOne[t],int(maxLeakAmount),"red")
    drawDots(canvas,t,time,pondTwo[t],int(maxLeakAmount),"blue")
    drawDots(canvas,t,time,pondThree[t],int(maxLeakAmount),"green")
    
## Wait until user kills graph window
win.wait()
