from turtle import *
import random

sam=Turtle()
colors=["green yellow","dark red","dark orchid","medium violet red","gold","coral","sienna","midnight blue","black"]

def draw_shape(num_sides):
    angle=360/num_sides
    for i in range(num_sides):
        sam.forward(100)
        sam.right(angle)

for j in range(3,11):
    sam.color(random.choice(colors))

    draw_shape(j)