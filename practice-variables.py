#1. Discounted Price

price = 99.99
discountPrice = 25
markdown = discountPrice/100 * price
price -= markdown
#price, discountPrice = 99.99, 25 #cannot add markdown since discountPrice and price haven't been initialized yet 
print("Price = {0:1.2f}".format(price))

#2. Gas Mileage

filling1 = 23456
filling2 = 23678
gallons = 10
#filling1, filling2, gallons = 23456, 23678, 10
distanceTraveled = filling2 - filling1
print("Distance traveled: {} Miles".format(distanceTraveled))
print("Gallons used = {}".format(gallons))
print("How many miles per gallon did the car average between two fillings?")
print("Answer: {0:1.3f} Miles/Gallon".format(distanceTraveled/gallons))

#3 Rectangle Area Calculator

#length = float(input("What is the length of the rectangle? "))
#width = float(input("What is the width of the rectangle? "))
#print("The rectangle's area is {0:1.3f}".format(length * width))

#4 Integer Portion of a Floating-Point Number

num = float(input("Enter a floating point number: "))
print("The decimal portion is: {0:1.0f}".format(num))

#5 Decimal Portion of a Floating-Point Number

num2 = float(input("Enter a floating point number: "))
print("The decimal portion is: {0:1.0f}".format(num))
