#In this program we use classes by drawing a square, circle and triangle. 

import turtle

def draw_square(some_turtle):

    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")

    #Create a turtle named Brad that draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(10)

    for i in range(30):
        draw_square(brad)
        brad.right(10)

##    angie = turtle.Turtle()
##    angie.shape("arrow")
##    angie.color("blue")
##    angie.circle(100)
##
##    leslie = turtle.Turtle()
##    leslie.shape("arrow")
##    leslie.color("black")
##
##    for i in range(3):
##        leslie.forward(100)
##        leslie.right(120)

    window.exitonclick()
    
draw_art()
