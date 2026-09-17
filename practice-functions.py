import math
import random
import sys

#1 Use math module
# a) Use input() function to request any two numbers.
# b) Use math module, fmod() to return the remainder of the user input.
# c) Print out the result as an integer.
# d) Implement the validation of denominator to be a non-zero number using exception handling.

numerator = int(input("Please enter a numerator: "))
denominator = int(input("Please enter a denominator: "))
if denominator !=0:
    result = int(math.fmod(numerator, denominator))
    print(numerator, " % ", denominator , " = ", result)
else:
    print("Denominator cannot be zero. Exit...")
    sys.exit()

#2 Using math and random modules
# a) Use random module, randint() to generate a random number in the range (1, 100).
# b) Use math module, isqrt() to round a square root number downwards to the nearest integer.
# c) Print out the result.

randomNumber = random.randint(1,100)
print(randomNumber)
number = int(input("Please enter a number: "))
# number = math.isqrt(number)
# number = math.floor(number)
print("Square root of ", number, " is: ",math.floor(math.isqrt(number)))
#this is how we chain math methods

#3 Write a function hello() that prints “Hello World” to the console. Implement the code to test the function.

def hello():
    print("Hello World")

hello()

#4 Modify the function, hello() above with a parameter.
# a) Define the function, helloNum(n) with a loop to call hello() n times to the console.
# b) Use the parameter, n for the numbers of iterations in the loop.

def helloNum(n):
    while n!=0:
        hello()
        n-=1

count = int(input("Please enter a counter: "))
helloNum(count)

#5 Write a program that creates a void function to display a given message. Implement the code to test the function.
# a) message(p1, p2) uses a loop to print the text stored in p1, p2 times to the console.
# b) Define a main() function to do the following:
# 1) Request and print an input text from the console and print the text.
# 2) Get a random integer number, n, in the range (1, 10) and print n.
# 3) Call message() function with arguments, text and n.
# 4) Handle all input and output.
# c) Call main() function to initiate the tasks to be performed
