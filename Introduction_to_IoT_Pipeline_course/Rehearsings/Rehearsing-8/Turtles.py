import turtle
from turtle import *
from random import randint
pensize(50)
colormode(255)
sipi = turtle.Turtle()
print(sipi)
turtle.colormode(255)
r = 10
while True:
     
    # randint will have random color based on 
    # every randint the color will be called
    color(randint(0, 255), 
          randint(0, 255), 
          randint(0, 255))
    begin_fill()
    end_fill()
    for i in range(100):
        sipi.circle(r+i,45)