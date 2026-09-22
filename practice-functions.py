import math
import random
import sys
#1 Use math module
# a) Use input() function to request any two numbers.
# b) Use math module, fmod() to return the remainder of the user input.
# c) Print out the result as an integer.
# d) Implement the validation of denominator to be a non-zero number using exception handling.

# numerator = int(input("Please enter a numerator: "))
# denominator = int(input("Please enter a denominator: "))
# if denominator !=0:
#     result = int(math.fmod(numerator, denominator))
#     print(numerator, " % ", denominator , " = ", result)
# else:
#     print("Denominator cannot be zero. Exit...")
#     sys.exit()

#2 Using math and random modules
# a) Use random module, randint() to generate a random number in the range (1, 100).
# b) Use math module, isqrt() to round a square root number downwards to the nearest integer.
# c) Print out the result.

# randomNumber = random.randint(1,100)
# print(randomNumber)
# number = int(input("Please enter a number: "))
# # number = math.isqrt(number)
# # number = math.floor(number)
# print("Square root of ", number, " is: ",math.floor(math.isqrt(number)))
# #this is how we chain math methods

# #3 Write a function hello() that prints “Hello World” to the console. Implement the code to test the function.

# def hello():
#     print("Hello World")

# hello()

# #4 Modify the function, hello() above with a parameter.
# # a) Define the function, helloNum(n) with a loop to call hello() n times to the console.
# # b) Use the parameter, n for the numbers of iterations in the loop.

# def helloNum(n):
#     while n!=0:
#         hello()
#         n-=1

#def helloNum(n):
    # for i in range(n):
    #     hello()
# count = int(input("Please enter a counter: "))
# helloNum(count)

#5 Write a program that creates a void function to display a given message. Implement the code to test the function.
# a) message(p1, p2) uses a loop to print the text stored in p1, p2 times to the console.
# b) Define a main() function to do the following:
# 1) Request and print an input text from the console and print the text.
# 2) Get a random integer number, n, in the range (1, 10) and print n.
# 3) Call message() function with arguments, text and n.
# 4) Handle all input and output.
# c) Call main() function to initiate the tasks to be performed

# def message(p1, p2):
#     while p2>0:
#         print(p1)
#         p2-=1

# def main():
#     text = input("Please enter a string: ")
#     print(text)
#     n = random.randint(1,10)
#     print(n)
#     message(text,n)

# main()

#6 Name format.
# a) Define a function nameFormat() with parameters first, middle, and last.
# 1) This function prints the first name, the middle initial and the last name using proper title format.
# b) Define a main() function to do the following:
# 1) Call the function nameFormat with these positional arguments: john stu smith
# 2) Call the function nameFormat with these keyword arguments:
# last = ‘kennedy’, first = ‘john’, middle = ‘fitzgerald’
# c) Call main() function to initiate the tasks to be performed

def nameFormat(first, middle, last):
    # print(first.capitalize(), "", middle[0].capitalize() + ".", last.capitalize())
    print(first.title(), "", middle[0].title() + ".", last.title())

def main():
    nameFormat("John", "stu", "smith")
    nameFormat(last = 'kennedy', first = 'john', middle = 'fitzgerald')

main()

#7 is the same as 6

#8. Write a program that creates a list-returned function to display a list containing all but the first and last
# elements. Implement the code to test the function.
# a) Define a function, middle(l) with a list as the parameter:
# 1) middle(l) slices and constructs the list parameter.
# 2) middle(l) returns a new list that contains all but the first and last elements.
# For example, middle([1,2,3,4]) should return [2,3].
# b) Define a main() function to do the following:
# 1) Create a list, numList with n numbers in the list.
# 2) Get a random integer, n, in the range (1, 10).
# 3) Call middle(numList) function and print the returned list.
# 4) Handle all input and output.
# c) Call main() function to initiate the tasks to be performed.

# def middle(l):
#     m = len(l)
#     #need to check if the length of m = 1. if it is needs to print [1] twice
#     if m == 1:
#         print("No change to made to the list")
#         print("List Length:", m)
#         print(l[:])
#         print(l[:])
#     else:
#         print("List Length:", m)
#         print(l[:])
#         print(l[1:m-1])

# def main():
#     #take the random number n. use a while loop while(i<=n) and i starting from 1 add it to the list
#     n = random.randint(1,10)
#     numlist = []
#     i = 1
#     while i<=n:
#         numlist.append(i)
#         i += 1
#     middle(numlist)

# main()
