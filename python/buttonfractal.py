from tkinter import*
import turtle


t = turtle.Turtle()
t.speed(0)
def koch(t, order, size):
    if order == 0: # The base case is just a straight line
        t.forward(size)
    else:
        koch(t, order-1, size/3) # Go 1/3 of the way
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)
def snowflake():
    kochsnowflake(t,2,100)

def kochsnowflake(t,order,size):
    for i in range(3):
        t.right(120)
        koch(t,order,size)

tk = Tk()
btn = Button(tk, text ='click me', command=snowflake)
btn.pack()
mainloop()


