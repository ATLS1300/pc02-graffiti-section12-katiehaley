#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Katie Haley
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

turtle.penup()
turtle.goto(111,-90)
turtle.seth(45)
turtle.pendown()
turtle.pensize(10)
turtle.pencolor("yellow")
turtle.forward(75)
turtle.left(110)
turtle.forward(30)
turtle.right(110)
turtle.forward(75)
turtle.right(65)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.left(110)
turtle.forward(30)
turtle.goto(111,-90)
turtle.penup()

turtle.goto(300,20)
turtle.pendown()
turtle.pensize(3)
turtle.color("red")
turtle.left(60)
turtle.forward(50)
turtle.penup()

turtle.goto(280,-50)
turtle.pendown()
turtle.pensize(3)
turtle.color("blue")
turtle.right(45)
turtle.forward(60)
turtle.penup()

turtle.goto(120,50)
turtle.pendown()
turtle.color("violet")
turtle.left(145)
turtle.forward(40)
turtle.penup()

turtle.goto(200,80)
turtle.pendown()
turtle.color("green")
turtle.right(45)
turtle.forward(60)
turtle.penup()

turtle.goto(270,70)
turtle.pendown()
turtle.color("orange")
turtle.right(30)
turtle.forward(50)
turtle.penup()

turtle.goto(135,160)
turtle.pendown()
turtle.pensize(15)
turtle.color("yellow")
turtle.circle(4)
turtle.penup()

turtle.goto(250,160)
turtle.pendown()
turtle.pensize(15)
turtle.color("yellow")
turtle.circle(4)
turtle.penup()

turtle.goto(340,80)
turtle.pendown()
turtle.pensize(15)
turtle.color("yellow")
turtle.circle(4)
turtle.penup()

turtle.goto(355,-15)
turtle.pendown()
turtle.pensize(15)
turtle.color("yellow")
turtle.circle(4)
turtle.penup()































#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
