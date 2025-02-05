import turtle

window = turtle.Screen()
window.bgcolor('red')

pointer = turtle.Turtle()

for color in ['white', 'black', 'brown', 'yellow']:
    pointer.color(color)
    pointer.forward(200)
    pointer.left(90)

window.mainloop()
