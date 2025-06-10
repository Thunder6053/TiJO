class Figure:
    def __init__(self, name, color="#808080"):
        self.name = name
        self.color = color

    def change_color(self, new_color):
        self.color = new_color

    def to_dict(self):
        return {self.name: self.color}


class Square(Figure):
    def __init__(self):
        super().__init__("square")


class Circle(Figure):
    def __init__(self):
        super().__init__("circle")


class Triangle(Figure):
    def __init__(self):
        super().__init__("triangle")