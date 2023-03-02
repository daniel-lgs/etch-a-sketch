from turtle import Turtle, Screen

my_arrow = Turtle()
my_screen = Screen()


def forward():
    my_arrow.forward(5)


def backward():
    my_arrow.backward(5)


def counter_clockwise():
    my_arrow.left(5)


def clockwise():
    my_arrow.right(5)


def clear():
    my_arrow.setposition(0, 0)
    my_arrow.clear()


my_screen.listen()

my_screen.onkeypress(forward, "Up")
my_screen.onkeypress(backward, "Down")
my_screen.onkeypress(counter_clockwise, "Left")
my_screen.onkeypress(clockwise, "Right")
my_screen.onkeypress(clear, "c")

my_screen.exitonclick()
