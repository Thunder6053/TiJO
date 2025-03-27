# Naruszona zasada OCP

class Figure():
    def draw(self):
        pass

# Klasa reprezentująca kwadrat
class Square(Figure):
    def __init__(self, a):
        self.a = a

    def draw(self):
        for _ in range(self.a):
            print(self.a * "o ")
        print()


# Klasa reprezentująca trójkąt
class Triangle(Figure):
    def __init__(self, h):
        self.h = h

    def draw(self):
        for i in range(1, self.h + 1):
            print(i * "o ")
        print()


# Klasa rysująca figury (nie wymaga modyfikacji przy dodawaniu nowych figur)
class FigureDrawer:
    def draw(self, figure: Figure):
        figure.draw()


a = 5
h = 5

square = Square(a)
triangle = Triangle(h)

drawer = FigureDrawer()
drawer.draw(square)
drawer.draw(triangle)