# Your name: Bailey Ellul
# Your student id: 19398388
# Your email: bellul@umich.edu
# List who or what you worked with on this homework:
# If you used generative AI also include how you used it.
# Did your use of GenAI on this assignment align with your goals and guidelines in your Gen AI contract? If not, why?
#I used no ai
# import the turtle functions for use in this program
from turtle import *

### write all new functions here ###
def draw_initials(turtle):
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(30)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.penup()
    turtle.goto(40,0)
    turtle.pendown()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.penup()
    turtle.goto(40,0)
    turtle.pendown()
    turtle.forward(30)
    turtle.penup()
    turtle.goto(40,-15)
    turtle.pendown()
    turtle.forward(15)


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
def draw_triangle(turtle, color, x_position, y_position, length, heading):
    turtle.penup()
    turtle.goto(x_position, y_position)
    turtle.setheading(heading)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)
    turtle.end_fill()

def draw_line(turtle, color, x_position, y_position, length,heading):
    turtle.penup()
    turtle.goto(x_position, y_position)
    turtle.pendown()
    turtle.setheading(heading)
    turtle.color(color)

    turtle.pensize(5)
    turtle.forward(length)

def draw_snow_globe(turtle):
    draw_circle(turtle, 'light blue', 0, 0, 150)
    draw_rectangle(turtle, 'brown', -150, 30, 300, 70)
    draw_circle(turtle, 'white', 0, 180, 30)
    draw_circle(turtle, 'white', 0, 120, 40)
    draw_circle(turtle, 'white', 0, 80, 50)
    draw_line(turtle, 'brown', -40, 180, 30,135)
    draw_line(turtle, 'brown', 40, 180, 30,45)
    draw_line(turtle, 'black', 15, 220, 5,90)
    draw_line(turtle, 'black', -15, 220, 5,90)
    draw_line(turtle, 'pink', 0, 0, 30,-90)
    draw_line(turtle, 'pink', 0, 0, 30,-90)
    draw_line(turtle, 'pink', 0, -30, 30,0)
    draw_line(turtle, 'pink', 30, -30, 15,90)
    draw_line(turtle, 'pink', 30, -15, 30,180)
    draw_line(turtle, 'pink', 0, 0, 15,0)
    draw_line(turtle, 'pink', 15, 0, 15,-90)
    draw_line(turtle, 'pink', 40, 0, 30,-90)
    draw_line(turtle, 'pink', 40, -30, 30,0)
    draw_line(turtle, 'pink', 40, 0, 30,0)
    draw_line(turtle, 'pink', 40, -15, 15,0)


    draw_triangle(turtle, 'orange', 0, 215, 15, -90)

    
    
def main():
    space = Screen()
    space.bgcolor('#3A3B3C')
    turtle = Turtle()
    draw_snow_globe(turtle)
    space.exitonclick()
    

    pass


# Only run the main function if this file is executed (not imported)
if __name__ == '__main__':
    main()
