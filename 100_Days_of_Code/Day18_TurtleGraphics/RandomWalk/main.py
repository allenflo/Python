import turtle
from turtle import Turtle, Screen
import random

colors = ["red", "purple", "blue", "orange", "green", "yellow"]
directions = [0, 90, 180, 270]

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.pensize(10)
# tim.width(10)
tim.speed(10)

for i in range(0,100):
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.color(random.choice(colors))

screen = Screen()
screen.exitonclick()

