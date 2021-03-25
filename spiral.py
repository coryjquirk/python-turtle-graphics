 # https://www.geeksforgeeks.org/draw-black-spiral-pattern-using-turtle-in-python/
# import turtle
import turtle

turtle.bgcolor('black')
turtle.title('spiral')
# initialising variables
dist = 1
flag = 1000
  
# initialising turtle
spiral = turtle.Pen()
spiral.width(2)
# changing speed of turtle
spiral.speed(1000)
# making patten
while flag:
    
    # makes the turtle to move forward
    spiral.forward(dist)
    spiral.pencolor("#1a81f7")
    # makes the turtle to move left
    spiral.left(130)
    spiral.left(2)
    dist += 1
    flag -= 1
    
    # makes the turtle to move forward
    spiral.forward(dist)
    spiral.pencolor("red")
    # makes the turtle to move left
    spiral.left(130)
    spiral.left(1)
    dist += 1
    flag -= 1

    # makes the turtle to move forward
    spiral.forward(dist)
    spiral.pencolor("#fcd588")
    # makes the turtle to move left
    spiral.left(130)
    spiral.left(2)
    dist += 1
    flag -= 1

    # makes the turtle to move forward
    spiral.forward(dist)
    spiral.pencolor("#fe9909")
    # makes the turtle to move left
    spiral.left(130)
    spiral.left(1)
    dist += 1
    flag -= 1

    # makes the turtle to move forward
    spiral.forward(dist)
    spiral.pencolor("purple")
    # makes the turtle to move left
    spiral.left(130)
    spiral.left(2)
    dist += 1
    flag -= 1
