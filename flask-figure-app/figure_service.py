from figures import Square, Circle, Triangle

class FigureService:
    def __init__(self):
        self.figures = {
            "square": Square(),
            "circle": Circle(),
            "triangle": Triangle()
        }

    def change_color(self, figure_type, new_color):
        if figure_type in self.figures:
            self.figures[figure_type].change_color(new_color)
            return True
        return False

    def change_color_all(self, new_color):
        for figure in self.figures.values():
            figure.change_color(new_color)

    def get_all_colors(self):
        return {name: figure.color for name, figure in self.figures.items()}
