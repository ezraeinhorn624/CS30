from turtle import *
import time
'''
Description: Turtle Homework 3
Written By: Avery Einhorn
Date: 11/1/18
'''
# I've implemented this function for you; do not edit it.
def tree( trunkLength, angle, levels ):
    left(90)
    sidewaysTree(trunkLength, angle, levels)

# This is the function you have to implement.
def sidewaysTree( trunkLength, angle, levels ):
    if levels==0:
        return
    forward(trunkLength)
    left(angle)
    sidewaysTree(trunkLength/2,angle,levels-1)
    right(angle)
    right(angle)
    sidewaysTree(trunkLength/2,angle,levels-1)
    left(angle)
    backward(trunkLength)
    """ draws a sideways tree
        trunklength = the length of the first line drawn ("the trunk")
        angle = the angle to turn before drawing a branch
        levels = the depth of recursion to which it continues branching
    """
    return