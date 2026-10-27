#1. Class Implementation.
# 01) Implement a class Rectangle with two attributes, width and height.
# 02) Define an init method for Rectangle class to initialize the attribute values via parameters.
# 03) Implement a display() method to print the values of width and height.
# 04) Instantiate two objects of type rectangle: one with attribute values 4 and 5, and the other with attribute
# values 10 and 10.
# r1 = Rectangle(4, 5)
# r2 = Rectangle(10, 10)
# 05) Call the display() method to print width and height for both objects.
# 06) Access and print the width attribute value of r1 and the height attribute value of r2.

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def display(self):
#         print(f"Width: {self.width}")
#         print(f"Height: {self.height}")

# r1 = Rectangle(4,5)
# r2 = Rectangle(10,10)
# r1.display()
# r2.display()

#2. Class modification.
# 01) Modify the __init__ method for Rectangle class to include optional parameters with default value of 0
# for both width and height.
# 02) Implement __str__ method to return a formatted string showing the width and height values as
# displayed below.
# 03) Instantiate two objects of type rectangle, one without attributes, and the other with attribute values 11
# and 12.
# 04) Use the print() function to display both objects created above.

# class Rectangle:
#     def __init__(self, width = 0, height = 0):
#         self.width = width
#         self.height = height

#     def __str__(self):
#         return (f"Rectangle:\nWidth: {self.width} & Height: {self.height}")
    
#     def display(self):
#         print(f"Width: {self.width}")
#         print(f"Height: {self.height}")
# r3 = Rectangle()
# r3.display()
# print(r3)
# r4 = Rectangle(11,12)
# r4.display()
# print(r4)


# from rectangle import Rectangle

# r1 = Rectangle(4, 5)
# r2 = Rectangle()

# r1.display()
# r2.display()

# print(r1.area())
# print(r2.area())

# r2.setWidth(6)
# r2.setHeight(6)

# print(r2.getWidth())
# print(r2.getHeight())
# print(r2.area())

from shapes import Rectangle, Circle

# Rectangle
r = Rectangle()
r.display()
r.setWidth(1.25)
r.setHeight(1.25)
print("Get Width:", r.getWidth())
print("Get Height:", r.getHeight())
print(f"Area: {r.area():.5f}")

# Circle
c = Circle(0)
c.display() 
c.setRadius(10)
print("Get Radius:", c.getRadius()) 
print(f"Area: {c.area():.5f}")
print(f"Circumference: {c.circumference():.5f}")