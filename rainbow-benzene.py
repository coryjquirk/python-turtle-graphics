# Python program to draw  
# Rainbow Benzene 
# using Turtle Programming
# https://www.codium.co.in/2020/07/rainbow-benzene-tutorial-turtle-python.html
import turtle 
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
t = turtle.Pen() 
turtle.bgcolor('black') 
for x in range(360): 
    t.pencolor(colors[x%6]) 
    t.width(x/100 + 1) 
    t.forward(x) 
    t.left(59)
