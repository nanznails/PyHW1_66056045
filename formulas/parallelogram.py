from formulas.shape import Shape
class Parallelogram(Shape):

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.paral_area = 0.0

    def __str__(self) -> str:
        return 'Parallelogram Area width ' + str(self.width) + ' height ' + str(self.height) + ' is ' + str(self.area())
    def area(self):
        self.paral_area = self.width * self.height
        return self.paral_area