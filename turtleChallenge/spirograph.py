import turtle as t
import random

sam=t.Turtle()
t.colormode(255)

def color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color_pick=(r,g,b)
    return color_pick
sam.speed("fastest")
def draw_spirograph(gap):
    for i in range(int(360/gap)):
        sam.color(color())
        sam.circle(100)
        sam.setheading(sam.heading()+gap)
        
draw_spirograph(5)


screen=t.Screen()
screen.exitonclick()