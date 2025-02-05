import turtle

def draw_square(pointer, size):
    """
        You can put in what does this function do. It's called doc string and
        is used as a documentation.
    """
    pointer.shape('turtle')
    pointer.color('white')

    for i in range(4):
        pointer.forward(size)
        pointer.left(90)

window = turtle.Screen()
window.bgcolor('black')

draw_square(turtle.Turtle(), 200)

window.mainloop()
