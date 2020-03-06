from turtle import *
import time
'''
Description: HW2, turtle problems
Written By: Avery Einhorn
Date: 10/16/18
'''

def helperRegularNGon(n,sideLength,angle):
    if n!=0:
        forward(sideLength)
        left(angle)
        time.sleep(.05)
        helperRegularNGon(n-1,sideLength,angle)
    else:
        return #draws an ngon using 360/n as an angle change
def regularNGon(n, sideLength): #calls helper which includes an angle operator
    helperRegularNGon(n,sideLength,360/n)
regularNGon(12,80)
time.sleep(2)
reset()

def archSpiral(initialLen, increment, angle, n):
    if n==0:
        return
    else:
        forward(initialLen)
        left(angle)        
        archSpiral(initialLen+increment,increment,angle,n-1) #spirals out each segment with an additive increment
archSpiral(1,.1,20,500)
time.sleep(2)
reset()
def logSpiral(initialLen, percentIncrease, angle, n): #spirals out each segment with a multiplicative increment
    if n==0:
        return
    else:
        forward(initialLen)
        left(angle)
        #time.sleep(0.05)
        logSpiral((initialLen*(percentIncrease/100.00000+1)),percentIncrease,angle,n-1)
        #Decimals after the '/100' serve to float the whole thing
logSpiral(1,4,20,130)