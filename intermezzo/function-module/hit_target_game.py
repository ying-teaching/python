
import turtle

TARGET_LLEFT_X = 100  # Target's lower-left X
TARGET_LLEFT_Y = 250  # Target's lower-left Y
TARGET_WIDTH = 25     # Width of the target

from game_constants import MAX_DISTANCE

# define constants locally if they are not shared
def draw_target(pen):
    EAST = 0              # Angle of east direction
    NORTH = 90            # Angle of north direction
    SOUTH = 270           # Angle of south direction
    WEST = 180            # Angle of west direction
    PROJECTILE_SPEED = 1  # Projectile's animation speed



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

    pen.home()
    pen.showturtle()
    pen.speed(PROJECTILE_SPEED)

def get_angle_distance():
    angle = int(input("Enter the projectile's angle 0-360: "))
    distance = int(input(f'Enter the launch distance (1-{MAX_DISTANCE}): '))
    return angle, distance

def launch_turtle(pen, angle, distance):
    pen.setheading(angle)
    pen.pendown()
    pen.forward(distance)

def show_hit_message(pen):
    xcor = pen.xcor()
    ycor = pen.ycor()

    # Did it hit the target?
    is_in_x = ((xcor >= TARGET_LLEFT_X) and 
        (xcor <= (TARGET_LLEFT_X + TARGET_WIDTH)))
    is_in_y = ((ycor >= TARGET_LLEFT_Y) and
        (ycor <= (TARGET_LLEFT_Y + TARGET_WIDTH)))
    is_hit = is_in_x and is_in_y

    # show message
    if is_hit:
        print('Target hit!')
    else:
        print('You missed the target.')

def test_get_angle_distance():
    angle, distance = get_angle_distance()
    print(angle, distance)

def run_game(pen):

    draw_target(pen)

    angle, distance = get_angle_distance()

    launch_turtle(pen, angle, distance)

    show_hit_message(pen)

if __name__ == '__main__':
    test_get_angle_distance()
