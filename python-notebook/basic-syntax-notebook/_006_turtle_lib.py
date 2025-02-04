# This line tells python to load a module named turtle.
# Python is case sensitive so module Turtle and turtle are different.
import turtle

window_background_color = input("Enter the screen background color: ")

# First we create a window using the turtle.Screen() module.
window = turtle.Screen()
window.bgcolor(window_background_color)
window.title('Turtle Experiment')

pointer_color = input("Enter the turtle color: ")
pensize = int(input("Enter the pensize: "))

# Turtle is like a pointer and a tail.
alex = turtle.Turtle()
alex.color(pointer_color)
alex.pensize(pensize)

# Now we will instruct the pointer to draw a shape
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)

window.mainloop()             # Wait for user to close window
