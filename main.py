import turtle

START_Y = -400

SCALE_FACTOR = .5
EDGE_LENGTH = 400
turtle.speed(100)


def drawTriangle(count = 8, scale = SCALE_FACTOR):
    if count == 0:
        return
    pos = turtle.pos()

    turtle.left(120)

    turtle.forward(EDGE_LENGTH * scale)
    drawTriangle(count - 1, scale * SCALE_FACTOR)
    turtle.forward(EDGE_LENGTH * scale)

    turtle.right(120)

    turtle.forward(EDGE_LENGTH * scale)
    drawTriangle(count - 1, scale * SCALE_FACTOR)
    turtle.forward(EDGE_LENGTH * scale)

    turtle.right(120)

    turtle.forward(EDGE_LENGTH * scale)
    drawTriangle(count - 1, scale * SCALE_FACTOR)
    turtle.forward(EDGE_LENGTH * scale)

    turtle.left(120)

turtle.penup()
turtle.goto(0, START_Y)
turtle.pendown()
drawTriangle()
turtle.penup()
input()