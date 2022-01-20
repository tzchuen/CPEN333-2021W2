# Student name: Zhi Chuen Tan
# Student number: 65408361

import turtle

# HEX codes of Olympic Ring Colours
# taken from: https://www.flagcolorcodes.com/olympic-rings-flag 
olympic_blue = "#0081C8"
olympic_yellow = "#FCB131"
olympic_black = "#000000"
olympic_green = "#00A651"
olympic_red = "#EE334E"

# declare constants 
radius = 45
gap = 10 # gap between each ring
pen_size = 7

# list of colours of each ring
colours = [olympic_blue, olympic_black, olympic_red, olympic_yellow, olympic_green]

# list of coordinates to put start drawing, assuming (0,0) is the centre of the black ring
positions = [(-(2*radius + gap), -radius), (0, -radius), (2*radius + gap, -radius), (-(radius + 0.5*gap), -2*radius), (radius + 0.5*gap, -2*radius)]


# set pensize
turtle.pensize(pen_size)

# make sure nothing is draw
turtle.penup()

for i in range (0, 5):
    turtle.goto(positions[i])   # move pen to position i
    turtle.color(colours[i])    # set pen colour to ring colour
    turtle.pendown()            
    turtle.circle(radius)       # draw ring
    turtle.penup()              # stop drawing ring

turtle.hideturtle()
turtle.done()

