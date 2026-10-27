from math import pi


class Rectangle:
    def __init__(self, width=1, height=1, type="rectangle"):
        self._width = width
        self._height = height
        self._type = type

    def display(self):
        print(f"Width: {self._width}")
        print(f"Height: {self._height}")

    def setWidth(self, w):
        self._width = w

    def setHeight(self, h):
        self._height = h

    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height

    def area(self):
        return self._width * self._height


class Circle:
    def __init__(self, radius=1, type="circle"):
        self._radius = radius
        self._type = type

    def display(self):
        print(f"Radius: {self._radius}")

    def setRadius(self, r):
        self._radius = r

    def getRadius(self):
        return self._radius

    def area(self):
        return pi * self._radius ** 2

    def circumference(self):
        return 2 * pi * self._radius