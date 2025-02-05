import turtle

def draw_square(pointer, size, same_spot):

    for i in range(4):
        pointer.forward(size)
        pointer.left(90)

    if not same_spot:
        pointer.penup()
        pointer.forward(40)
        pointer.pendown()

window = turtle.Screen()

pointer = turtle.Turtle()
for i in range(5):
    print('You can comment out the next line to draw pattern')
    #draw_square(pointer, 20, False)

def create_a_square_of_size(pointer, size):

        for i in range(4):
            pointer.forward(size)
            pointer.left(90)

        pointer.left(-135)
        pointer.penup()
        pointer.forward(15)
        pointer.pendown()
        pointer.left(135)

for i in range(20, 120, 20):
    print('You can comment out the next line to draw pattern')
    #create_a_square_of_size(pointer, i)

def draw_polygon(pointer):
    for i in range(8):
        pointer.forward(30)
        pointer.left(45)

#draw_polygon(pointer)

def draw_flower(pointer):
    for i in range(20):
        draw_square(pointer, 50, True)
        pointer.left(18)

#draw_flower(pointer)

def draw_spiral(pointer, twist):
    for i in range(1, 401, 5):
        pointer.left(-90 + twist)
        pointer.forward(i);



#draw_spiral(pointer, 0)
#draw_spiral(pointer, 1)

def draw_circle(pointer, radius):

    pointer.penup()
    pointer.forward(radius)
    pointer.pendown()

    for i in range(180):
        pointer.left(3.14159)
        pointer.forward(radius)

#draw_circle(pointer, 5)

def draw_star(pointer):

    pointer.left(45)
    for i in range(5):
        pointer.forward(100)
        pointer.left(144)

#draw_star(pointer)

window.mainloop()
