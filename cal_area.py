#cal_area
from formulas.circle import Circle
from formulas.parallelogram import Parallelogram
from formulas.triangle import Triangle
from formulas.oval import Oval

if __name__ == '__main__':
    cc1 = Circle(3)
    print(cc1)

    ov1 = Oval(2, 5)
    print(ov1)

    tria1 = Triangle(3, 5)
    print(tria1)

    paral1 = Parallelogram(2, 7)
    print(paral1)