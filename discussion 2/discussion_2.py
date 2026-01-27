from turtle import *

### write all new functions here ###
def draw_circle(turtle, color, x_position, y_position, radius):
    turtle.penup()
    turtle.goto(x_position, y_position)
    turtle.pendown()
    
    turtle.color(color)
    
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rectangle(turtle, color, x_position, y_position, length, width):
     turtle.penup()
     turtle.goto(x_position, y_position)
     turtle.pendown()
     
     turtle.color(color)

     turtle.begin_fill()
     for i in range(2):
         turtle.forward(length)
         turtle.right(90)
         turtle.forward(width)
         turtle.right(90)
     turtle.end_fill()


def draw_elipse(turtle, color, x_position, y_position, radius):
    
    turtle.penup()
    turtle.goto(x_position, y_position)
    turtle.pendown()
     
    turtle.color(color)

    turtle.begin_fill()
    for i in range(2):
        turtle.circle(radius, 90)
        turtle.circle(radius/2, 90)
    turtle.end_fill()
    
def draw_line(turtle, color, x_position, y_position, length):
    turtle.penup()
    turtle.goto(x_position, y_position)
    turtle.pendown()
     
    turtle.color(color)

    turtle.pensize(5)
    turtle.forward(length)
def draw_curve(turtle, color, x_position, y_position, radius):
    turtle.penup()
    turtle.goto(x_position, y_position)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.color(color)

    turtle.pensize(5)
    turtle.circle(radius, 180)


def draw_emoji(turtle):
    """
    Write a function to draw an emoji.
    """

    # draw_circle(turtle, 'yellow', 0, 0, 150)
    # draw_rectangle(turtle, 'green', 0, 0, 200, 100)
    # draw_elipse(turtle, 'white', 0, 0, 200)
    # draw_line(turtle, 'red',0, 0, 100)
    # draw_curve(turtle, 'orange', 0, 0, 100)

    draw_circle(turtle, 'yellow', 0, 0, 150)
    draw_circle(turtle, 'black', 75, 150, 20)
    draw_circle(turtle, 'black', -75, 150, 20)
    draw_circle(turtle, 'pink', -85, 90, 20)
    draw_circle(turtle, 'pink', 85, 90, 20)
    # draw_circle(turtle, 'black', 0, 25, 25)
    draw_curve(turtle, 'black', -50, 75, 50)

    
    

def main():
    """
    Make sure to create a Screen object, a Turtle object,
    and call draw_emoji.

    Also, make sure to call the .exitonclick() method on your Screen instance
    to stop the program from exiting until you close the drawing window.

    TIP: You can call the .bgcolor() method on your Screen instance to change
    the background color.

    """

    space = Screen()
    space.bgcolor('#3A3B3C')
    t = Turtle()
    draw_emoji(t)
    space.exitonclick()
    



if __name__ == '__main__':
    main()


