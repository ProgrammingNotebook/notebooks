import turtle

window = turtle.Screen()

pointer = turtle.Turtle()

# Range method executes from 0 - 3 for range(4)
for i in range(4):
    pointer.forward(100)
    pointer.left(90)

window.mainloop()
