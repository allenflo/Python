import turtle
from turtle import Turtle, Screen
import random

colors = ["red", "purple", "blue", "orange", "green", "yellow"]

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.pensize(10)
# tim.width(10)
tim.speed(10)

tim.forward(100)
random.choice("forward", "left", "right" )





screen = Screen()
screen.exitonclick()

