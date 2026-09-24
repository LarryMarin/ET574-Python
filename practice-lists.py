# 1. Use list methods to code below.
# 01) Create an empty list called n.
# 02) Add 2 and 4 into the list.
# 03) Print the list.
# 04) Add 0, 1 and 3 in proper order.
# 05) Print the list.
# 06) Add 5 in proper order.
# 07) Print the list.
# 08) Remove 0 from the list.
# 09) Print the list.
# 10) Remove and print 2 from the list.
# 11) Print the list.
# 12) Remove and print 4 from the list.
# 13) Print the list.
# 14) Add all the removed numbers and print the sum.
# 15) Change the first item to 100 and last item to 9.9.
# 16) Copy the list n to a newNum list.
# 17) Clear the list n.
# 18) Print the original list, n and the newNum list.
# 19) Delete the list n.

# 01) Create an empty list called n.
n = []
# 02) Add 2 and 4 into the list.
n.append(2)
n.append(4)
#another way to add them to the list
#n.extend([2,4])
# 03) Print the list.
print(n)
# 04) Add 0, 1 and 3 in proper order.
n.append(0)
n.append(1)
n.append(3)
#another way to add them into the list
#n.extend([0,1,3])
n.sort()
# 05) Print the list.
print(n)
# 06) Add 5 in proper order.
n.append(5)
# 07) Print the list.
print(n)
# 08) Remove 0 from the list.
# n.remove(0)
num0 = n.pop(0)
# 09) Print the list.
print(n)
# 10) Remove and print 2 from the list.
num1 = n.pop(n.index(2))
print(num1)
# 11) Print the list.
print(n)
# 12) Remove and print 4 from the list.
num2 = n.pop(n.index(4))
print(num2)
# 13) Print the list.
print(n)
# 14) Add all the removed numbers and print the sum.
print("The sum of all removed numbers is = ", num0+num1+num2)
# 15) Change the first item to 100 and last item to 9.9.
#this is how we edit a certain index of the list
n[0] = 100
n[-1] = 9.9
print(n)
# 16) Copy the list n to a newNum list.
#different ways to copy the list
#newNum = list(n)
#newNum = n[:]
newNum = n.copy()
# 17) Clear the list n.
n.clear()
# 18) Print the original list, n and the newNum list.
print(n)
print(newNum)
# 19) Delete the list n.
del n

# 2. Write the code and ensure that the output matches the format exactly as described below.
# 1) Create a list named courses containing the names of your current courses.
# 2) Print the list of courses.
# 3) Use the len function to print (where X is the number of courses in the list):
# I am taking X courses
# 4) Using indexing to print the first and last items in the list.
# 5) Using slicing to print the first four classes.
# 6) Using slicing to print the last four classes.
# 7) Using slicing to print the classes except the first and last.

courses = ["ET725", "ET581", "ET574", "ET506", "ET509"]
print(courses)
print("I am taking", len(courses), "courses.")
print(courses[0], courses[-1])
print(courses[0:4])
print(courses[-4:])
x = len(courses)
print(courses[1:x-1])

#3 Write a Python function named grade_statistics() that performs the following tasks:
# 01) Create an empty list named grades inside the function.
# 02) Add any five grades (including at least two grades below 60) one at a time to grades.
# 03) Print the current list of grades in the format:
# Current grades: [92, 51, 83, 37, 72]
# 04) Calculate the total of these grades by indexing them into the list (do not use sum () yet)
# 05) Use the total and the len () function to calculate the average.
# 06) Print the average with two decimal places in the format:
# Average: 67.00
# 07) Remove all failing grades (lower than 60) using two different methods
# a. Use the remove () method to delete one falling grade.
# b. Use del statement to delete another falling grade.
# 08) Print the updated list of grades in the format:
# Updated grades: [92, 83, 72]
# 09) Recalculate the average using the built-in functions, sum () and len ().
# 10) Print the updated average with three decimal places in the format:
# Updated Average: 82.333
# 11) Call the function at the end of your program to display the results

def grade_statistics():
    grades = []
    # grades.extend([100, 42, 56, 84, 73])
    grades.append(100)
    grades.append(42)
    grades.append(56)
    grades.append(84)
    grades.append(73)
    print("Current grades: ", grades)
    gradeSum = 0
    for grade in grades:
        gradeSum += grade
    average = gradeSum/len(grades)
    print(f"Average: {average:.2f}")
    grades.remove(42)
    del grades[grades.index(56)]
    print("Updated Grades: ", grades)
    gradeSum = sum(grades)
    average = gradeSum/len(grades)
    print(f"Updated Average: {average:.3f}")
grade_statistics()

#4a. Write a Python program that analyzes a sentence using two functions.
# 1) Define a function named get_sentence() that:
# a. Prompts the user to enter a sentence using input().
# b. Returns the sentence entered by the user.
# 2) Define a function named analyze_sentence() that:
# a. Accepts a sentence (string) as a parameter.
# b. Splits the sentence into words using .split().
# c. Counts the number of words using len().
# d. Prints the result in the format:
# 3) In your main program:
# a. Call get_sentence() to retrieve the user’s sentence.
# b. Pass the sentence as an argument to analyze_sentence().

def getSentence():
    userInput = input("Please enter a sentence: ")
    return userInput

def analyzeSentence(sentence=''):
    splitSentence = sentence.split(' ')
    print("Number of words:", len(splitSentence))
sent = getSentence()
analyzeSentence(sent)

#4b. Write a Python program that analyzes a sentence using two functions.
# 1) Define a function named get_sentence() that:
# a. Prompts the user to enter a sentence using input().
# b. Returns the sentence entered by the user.
# 2) Define a function named analyze_sentence() that:
# a. Accepts a sentence (string) as a parameter.
# b. Splits the sentence into words using .split().
# c. Counts the number of words using len().
# d. Counts the total number of characters (excluding spaces).
# e. Finds the longest word in the sentence.
# f. Prints the result in the format:
# 3) In your main program:
# a. Call get_sentence() to retrieve the user’s sentence.
# b. Pass the sentence as an argument to analyze_sentence().
# Input text can be any content. Just make sure to precisely match the output format below.
# Example Output
# Enter a sentence: Python makes programming fun
# Number of characters (excluding spaces): 26
# Longest word: programming

def get_sentence():
    userInput = input("Please enter a sentence: ")
    return userInput

def analyze_sentence(sentence=''):
    splitSentence = sentence.split(' ')
    numChars = 0
    for i in range(len(splitSentence)):
         numChars += len(splitSentence[i])
    print("Number of characters (exluding spaces):", numChars)

sentence = get_sentence()
analyze_sentence(sentence)
