#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#Conor Fletcher     
#Date
# 12/19/19


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl 
import time

#create turtle
drawer = trtl.Turtle("circle")

#Turns screen grey
wn = trtl.Screen()

wn.bgcolor("grey")

#variables
switch = False
count = 1
#movement functions
def up(): 
    drawer.setheading(90)
    drawer.forward(10)
def down(): 
    drawer.setheading(270)
    drawer.forward(10)
def right(): 
    drawer.setheading(0)
    drawer.forward(10)
def left():
    drawer.setheading(180)
    drawer.forward(10)
def penplus():
    global count
    drawer.pensize(count)
    count += 1
#Increace and decreace pen size
def penminus():
    global count 
    drawer.pensize(count )
    count -= 1 
def clear():
    wn.reset()
def red():
    drawer.pencolor("red")
    drawer.fillcolor("red")
def blue():
    drawer.pencolor("blue")
    drawer.fillcolor("blue")
def green():
    drawer.pencolor("green")
    drawer.fillcolor("green")
   


#switch for on/off drawing
def switch(): 
    global switch 
    if switch: 
        drawer.penup() 
        switch = False 
    else: 
        drawer.pendown() 
        switch = True


#color/drawing functions
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
wn.onkeypress(switch,"u")
wn.onkeypress(penplus,"o")
wn.onkeyrelease(penminus,"p")
wn.onkeyrelease(clear,"space")
wn.onkeypress(red,"1")
wn.onkeypress(blue,"2")
wn.onkeypress(green,"3")
#create screen

#bind to keypresses


#listen
wn.listen()

#mainloop

wn.mainloop()