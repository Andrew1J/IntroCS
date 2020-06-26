import random
import turtle
turtle.bgcolor('black')
def randomshape():
    length = random.randint(0,100)
    x = random.randint(1,5)
    if x == 1:
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
    if x == 2:
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
    if x == 3:
        turtle.forward(length)
        turtle.left(72)
        turtle.forward(length)
        turtle.left(72)
        turtle.forward(length)
        turtle.left(72)
        turtle.forward(length)
        turtle.left(72)
        turtle.forward(length)
        turtle.left(72)
    if x == 4:
        turtle.circle(length)
    if x == 5:
        turtle.forward(150)
        turtle.right(144)
        turtle.forward(150)
        turtle.right(144)
        turtle.forward(150)
        turtle.right(144)
        turtle.forward(150)
        turtle.right(144)
        turtle.forward(150)
        turtle.right(144)
def mycircle(red, green, blue):
    turtle.colormode(255)
    turtle.color(red, green, blue)
    turtle.begin_fill()
    randomshape()
    turtle.end_fill()
    turtle.up() # pick up pen
    x = random.randint(-300, 300)
    y = random.randint(-250, 250)
    h = random.randint(0, 360)
    turtle.setheading(h)# set heading to random direction
    turtle.goto(x,y)
    z = random.randint(0, 100)
    turtle.forward(z) # move a random number of pixels
    turtle.down() # pen down
def execute():
    for i in range(0, 100):
        r = random.randint(0,255)   
        g = random.randint(0,255)
        b = random.randint(0,255)
        mycircle(r,g,b) # feed a random color to the function
execute()
        
        
