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

# 2. Class modification.
# 01) Modify the __init__ method for Rectangle class to include optional parameters with default value of 0
# for both width and height.
# 02) Implement __str__ method to return a formatted string showing the width and height values as
# displayed below.
# 03) Instantiate two objects of type rectangle, one without attributes, and the other with attribute values 11
# and 12.
# 04) Use the print() function to display both objects created above.

# class Rectangle:
#     def __init__(self, width = 1, height = 1):
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
# w = int(input("Please enter the width: "))
# h = int(input("Please enter the height: "))
# r5 = Rectangle(w, h)
# r5.display()
# print(r5)

# 3. Import Class.
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
# g) Call area() in print() to display the area of r2.

from rectangle import Rectangle
r1 = Rectangle(4, 5)
r2 = Rectangle()

r1.display()
r2.display()

print(r1.area())
print(r2.area())

r2.setWidth(6)
r2.setHeight(6)

print(r2.getWidth())
print(r2.getHeight())
print(r2.area())

#4. 
# from shapes import Rectangle, Circle

# # Rectangle
# r = Rectangle()
# r.display()
# r.setWidth(1.25)
# r.setHeight(1.25)
# print("Get Width:", r.getWidth())
# print("Get Height:", r.getHeight())
# print(f"Area: {r.area():.5f}")

# # Circle
# c = Circle(0)
# c.display() 
# c.setRadius(10)
# print("Get Radius:", c.getRadius()) 
# print(f"Area: {c.area():.5f}")
# print(f"Circumference: {c.circumference():.5f}")
