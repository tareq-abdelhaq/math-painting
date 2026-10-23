from canvas import Canvas
from shapes import Rectangle, Square

width = int(input("Enter canvas width: "))
height = int(input("Enter canvas height: "))
color = input("Enter canvas color (white or black): ")
canvas_color = [0, 0, 0] if color.lower() == "black" else [255, 255, 255]

canvas = Canvas(width, height, canvas_color)


while True:
    answer = input("What do you like to draw? Enter quit to quit: ")
    if answer == "quit":
        break

    while answer.lower() not in ("square", "rectangle"):
        answer = input("Please provide a supported shape (square or rectangle): ")

    shape = answer.capitalize()
    x = int(input(f"Enter x of the {shape}: "))
    y = int(input(f"Enter y of the {shape}: "))

    red = int(input(f"How much red should the {shape} have? "))
    green = int(input(f"How much green should the {shape} have? "))
    blue = int(input(f"How much blue should the {shape} have? "))

    if shape == "Rectangle":
        rect_width = int(input(f"Enter the width of the {shape}: "))
        rect_height = int(input(f"Enter the height of the {shape}: "))
        rect = Rectangle(x, y, [red, green, blue], rect_width, rect_height)
        rect.draw(canvas)
    elif shape == "Square":
        side = int(input(f"Enter the side length of the {shape}: "))
        sq = Square(x, y, [red, green, blue], side)
        sq.draw(canvas)

canvas.make_img("canvas.png")
