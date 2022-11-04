import turtle as turtle_module
from turtle import Screen
import random

color_list = [(205, 1, 152), (194, 170, 10), (48, 197, 55), (59, 24, 214), (224, 55, 84), (224, 229, 54)]

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.penup()
tim.speed(0)
tim.goto(-200, -200)
tim.hideturtle()

def row():
    for i in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
        tim.dot(20, random.choice(color_list))

def left_turn():
    tim.left(90)
    tim.forward(50)
    tim.left(90)

def right_turn():
    tim.right(90)
    tim.forward(50)
    tim.right(90)

for i in range(5):
    row()
    left_turn()
    row()
    right_turn()

screen = Screen()
screen.exitonclick()

# import colorgram

# Extract 10 colors from image
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 10)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)