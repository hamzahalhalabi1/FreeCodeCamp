class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"

        return picture

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def get_amount_inside(self, shape):
        width_ratio = self.width // shape.width
        height_ratio = self.height // shape.height
        return width_ratio * height_ratio


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def set_side(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"
