# https://github.com/ythecombinator/python-homework

# Here we intend to create a simple different star which have two colors.
# It should use the turtle module
import turtle
# Let's give it a name.
mandala = turtle.Turtle()
# A random  name.
turtle.title("mandala")
# Set a dark color for the background.
turtle.bgcolor("black")
# Set the fastest speed
mandala.speed(10)
mandala.hideturtle()
# Define the number of iterations
n = 100

# The main function
def drawMandala(n):

  for i in range(n):

      turtle.penup()
      turtle.forward(100)
      turtle.left(90)
      turtle.penup()
      turtle.forward (30)
      turtle.left (110)
      turtle.pendown()
      turtle.pencolor ("#c874ff")
      turtle.forward (120)
      turtle.pencolor("#74ffc8")
      turtle.right (70)
      turtle.forward (70)
      turtle.right (40)
      turtle.forward (50)
      turtle.pensize(1)
      turtle.pencolor ("#abff74")
      turtle.left (60)
      turtle.pensize(5)
      turtle.forward (100)
      turtle.pencolor("#ff74ab")
      turtle.left(90)
      turtle.forward (100)
      turtle.right (50)
      turtle.forward (70)
      turtle.pensize(10)
      turtle.left (60)
      turtle.pensize(6)
      turtle.forward (65)
      turtle.left (45)
      turtle.forward (120)




# Perform the main fucntion
drawMandala(n)
