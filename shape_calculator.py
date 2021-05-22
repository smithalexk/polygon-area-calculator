class Rectangle(object):
    def __init__(self, in_w, in_h):
        self.width = in_w
        self.height = in_h

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, in_w):
        self._width = in_w

    @property
    def height(self):
        return self._height

    def __repr__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"

    @height.setter
    def height(self, in_h):
        self._height = in_h

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        hh = "*"*self.width + "\n"
        return hh * self.height
    
    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()



class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side
    
    def set_height(self, height):
        self.set_side(height)
    
    def set_width(self, width):
        self.set_side(width)
    

    def __repr__(self):
        return f"{self.__class__.__name__}(side={self.width})"
