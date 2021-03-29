# Import the turtle library for
# drawing the required curve
import turtle as spiro
spiro.title("spirograph")
# Set the background color as black,
# pensize as 2 and speed of drawing
# curve as 10(relative)
spiro.bgcolor('black')
spiro.pensize(2)
spiro.speed(10)

# Iterate six times in total
for i in range(600):

    # Choose your color combination
    for color in ('#875487', '#5c94ff', '#6597e6',
                  '#ee6d73', '#975eff', '#9d60ef',
                  '#f445a6'):
        spiro.color(color)

        # Draw a circle of chosen size, 100 here
        spiro.circle(100)

        # Move 10 pixels left to draw another circle
        spiro.left(10)

        # Hide the cursor(or turtle) which drew the circle
    spiro.hideturtle()
