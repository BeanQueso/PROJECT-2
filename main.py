'''
Parameter Picasso
Eshaan Tripathi
9/28/22
Takes parameters for amount of sides, side length, color, and coordinates to create a shape.
'''

#import turtle library
from turtle import *

#create procedure with the parameters of sides, side length, color, and coordinates to create a shape.
def drawShape(sides,sidelength,color,x,y):
    #lift pen up
    penup()
    #go to coordinates
    goto(x,y)
    #set pen down
    pendown()
    #go through each side
    for i in range(sides):
        #set the pen color as the color given as parameter
        pencolor(color)
        #go forward the sidelength
        forward(sidelength)
        #turn right the angle of 360 degrees divided by number of sides
        right(360/sides)  
    #make it so that the program exits when the user clicks on window.
    exitonclick()
    
#provide parameters and run function.
drawShape(8,60,"blue",50,70)