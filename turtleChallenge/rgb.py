import turtle as t
import random

sam=t.Turtle()
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color

directions=[0,90,180,270]
sam.pensize(15)
sam.speed("fastest")

for i in range(200):
    sam.color(random_color())
    sam.forward(30)
    sam.setheading(random.choice(directions))