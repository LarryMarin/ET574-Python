#4. Import Class.
# 01) Implement a class Rectangle with two attributes, width and height.
# 02) Implement an init method with the optional parameter type.
# Set the default value of the attributes of width and height to 1.
# 03) Implement a display method to print the values of width and height.
# 04) Implement a setWidth method to assign width to the instance variable.
# 05) Implement a setHeight method to assign height to the instance variable.
# 06) Implement a getWidth method to return the value of the instance variable width.
# 07) Implement a getHeight method to return the value of the instance variable height.
# 08) Implement an area method to return the value of area of a rectangle.
# 09) Save Rectangle class as rectangle.py.
# 10) Import Rectangle class from rectangle.py.
# 11) Employs the Rectangle class methods above to set and get various measurements of a rectangle.
# a) Instantiate two objects of type rectangle, one with arguments one without.
# r1 = Rectangle(4, 5)
# r2 = Rectangle()
# b) Call display() to print width and height.
# c) Call area() in print() to display the area of r1 and r2.
# d) Call setWidth() and setHeight() to update width and height to 6 of r2.
# e) Call getWidth() in print() to display the updated width of r2.
# f) Call getHeight() in print() to display the updated height of r2.
# g) Call area() in print() to display the area of r2

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