from turtle import Turtle, Screen
import random

tim = Turtle()

screen = Screen()
screen.colormode(255)

def making_square():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)

def making_dashed_line():
    x = 0
    for _ in range(3):
        tim.showturtle()           #make the turtle visible
        tim.pendown()    
        tim.forward(10)

        tim.hideturtle()
        tim.penup()
        x+=20
        tim.goto(x,0)

def making_geometric_shapes():

    num_sides = 3
    for _ in range(8):
        angle = 360 / num_sides

        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        for _ in range(num_sides):
            tim.pencolor(r,g,b)

            tim.right(angle)
            tim.forward(100)

        num_sides += 1

making_geometric_shapes()

screen.exitonclick()