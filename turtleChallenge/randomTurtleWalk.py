import turtle as t
import random

sam=t.Turtle()
colors=["green yellow","dark red","dark orchid","medium violet red","gold","coral","sienna","midnight blue","black"]
directions=[0,90,180,270]
sam.pensize(15)
sam.speed("fastest")

for i in range(300):
    sam.color(random.choice(colors))
    sam.forward(30)
    sam.setheading(random.choice(directions))


