# Hit the Target Game
import turtle

# Named constants
SCREEN_WIDTH = 600    # Screen width
SCREEN_HEIGHT = 600   # Screen height
TARGET_LLEFT_X = 100  # Target's lower-left X
TARGET_LLEFT_Y = 250  # Target's lower-left Y
TARGET_WIDTH = 25     # Width of the target
FORCE_FACTOR = 30     # Arbitrary force factor
PROJECTILE_SPEED = 1  # Projectile's animation speed
NORTH = 90            # Angle of north direction
SOUTH = 270           # Angle of south direction
EAST = 0              # Angle of east direction
WEST = 180            # Angle of west direction

# Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

pen = turtle.Pen()

# Draw the target.
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
pen.pendown()
pen.setheading(EAST)
pen.forward(TARGET_WIDTH)
pen.setheading(NORTH)
pen.forward(TARGET_WIDTH)
pen.setheading(WEST)
pen.forward(TARGET_WIDTH)
pen.setheading(SOUTH)
pen.forward(TARGET_WIDTH)
pen.penup()

# Center the turtle.
pen.home()
pen.showturtle()
pen.speed(PROJECTILE_SPEED)

# Get the angle and force from the user.
angle = turtle.numinput("Input","Enter the projectile's angle", minval=0, maxval=360)
force = turtle.numinput("Input", "Enter the launch force (1-10)", minval=1, maxval=10)

# Calculate the distance.
distance = force * FORCE_FACTOR

# Set the heading.
pen.setheading(angle)

# Launch the projectile.
pen.pendown()
pen.forward(distance)

xcor = pen.xcor()
ycor = pen.ycor()

# Did it hit the target?
if (xcor >= TARGET_LLEFT_X and
    xcor <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    ycor >= TARGET_LLEFT_Y and
    ycor <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('Target hit!')
else:
        print('You missed the target.')

turtle.done()
