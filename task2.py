import turtle
import math

screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)


def draw_tree(pen, branch_length, level):
    if level == 0:
        return

    pen.forward(branch_length)

    pen.left(45)
    draw_tree(pen, branch_length * math.sqrt(2) / 2, level - 1)
    pen.right(45)

    pen.right(45)
    draw_tree(pen, branch_length * math.sqrt(2) / 2, level - 1)
    pen.left(45)

    pen.backward(branch_length)


def main(level):
    pen.penup()
    pen.goto(0, -200)
    pen.pendown()
    pen.left(90) 
    draw_tree(pen, 100, level)
    screen.mainloop()


level = int(input("Введіть рівень рекурсії: "))
main(level)
