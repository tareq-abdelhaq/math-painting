from canvas import Canvas


class Shape:
    """
    Base object that acts as the base class for any specific shape
    """

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


class Rectangle(Shape):
    """
    Object represents rectangles and inherits the basics out of the Shape Object.
    """

    def __init__(self, x, y, color, width, height):
        super().__init__(x, y, color)

        self.width = width
        self.height = height

    def draw(self, canvas: Canvas):
        row_start = self.y
        row_end = row_start + self.height  # inclusive

        col_start = self.x
        col_end = col_start + self.width  # inclusive

        # apply to the canvas
        canvas.data[row_start : row_end + 1, col_start : col_end + 1] = self.color


class Square(Shape):
    """
    Object represents squares and inherits the basics out of the Shape Object.
    """

    def __init__(self, x, y, color, side):
        super().__init__(x, y, color)

        self.side = side

    def draw(self, canvas):
        row_start = self.y
        row_end = row_start + self.side  # inclusive

        col_start = self.x
        col_end = col_start + self.side  # inclusive

        # apply to the canvas
        canvas.data[row_start : row_end + 1, col_start : col_end + 1] = self.color
