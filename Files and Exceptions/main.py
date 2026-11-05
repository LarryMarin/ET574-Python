# 1. Course File
# Write a while loop that prompts users to enter the course titles they are currently taking. For each course
# title entered, display a confirmation message and record the title in a file named courses.txt. Each course title
# should appear on a new line in the file. The sentinel value 'quit' should be case-insensitive (e.g., 'Quit',
# 'QUIT', or 'quit' should all stop the loop).

# filename = 'Files and Exceptions/course.txt'
# userInput = input("Please enter a title (quit to exit): ")
# while userInput.lower() != "quit":
#     with open(filename, 'a') as file_object:
#         file_object.write(f"{userInput.title()}\n")
#         print(f'"{userInput.title()}" has been added to the list.')
#     userInput = input("Please enter a title (type quit to exit): ")

# 2. File Reading
# The file Presidents.txt contains the names of the first three U.S. presidents. Create functions to read and
# display the contents of the file to the console in the following two ways. Implement exception handling to
# manage the case where the file is not found (FileNotFoundError). Hint: One function may use a for loop to
# read line by line, and another may use the read() or readlines() method.

# filename = 'Files and Exceptions/President.txt'
# def readLoop():
#     try:
#         print("Using Loop---")
#         with open(filename, 'r') as file_object:
#             for line in file_object:
#                 print(line.rstrip())
#     except FileNotFoundError:
#         print("The file does not exist.")
            
# def readList():
#     try:
#         print("Using List---")
#         with open(filename) as file_object:
#             lines = file_object.readlines()
#         for line in lines:
#             print(line.rstrip())
#     except FileNotFoundError:
#         print("The file does not exist.")

# readLoop()
# readList()

# 3. File Writing in function
# Write a program that defines different functions to create and write content to files using the write() and
# writelines() methods

# filename2 = 'President2.txt'
# def writeSingle():
#     try:
#         with open(filename2, 'w') as file_object:
#             file_object.write("George Washington\n")
#             file_object.write("John Adams\n")
#             file_object.write()
#     except FileNotFoundError:
#         print("The file does not exist.")

# filename3 = 'President3.txt'
# def writeLines():
#     try:
#         names = ["George Washington\n", "John Adams\n", "Thomas Jefferson\n"]
#         with open(filename3, 'w') as file_object:
#             file_object.writelines(names)
#     except FileNotFoundError:
#         print("The file does not exist.")

# writeSingle()
# writeLines()

# 4. File Writing, Appending, and Reading.
# a) Define a function to write names of any three US presidents to a text file.
# b) Define a function to append the names of any three additional US presidents to the same file created in
# part a).
# c) Define a function to read and display the contents of the file created in part b).
# d) Save all functions above in a module file.
# e) Define a main() function to import the module and calls the functions above, implementing appropriate
# exception handling.
# f) Call the main() function to execute the tasks

filename4 = 'Presidents.txt'
def writePres():
    try:
        with open(filename4, 'w') as file_object:
            file_object.write("George Washington\n")
            file_object.write("John Adams\n")
            file_object.write("Theodore Roosevelt\n")
    except FileNotFoundError:
        print("The file does not exist.")

def appendPres():
    try:
        with open(filename4, 'a') as file_object:
            file_object.write("James Madison\n")
            file_object.write("James Monroe\n")
            file_object.write("John Quincy Adams\n")
    except FileNotFoundError:
        print("The file does not exist.")

def readFile():
    try:
        with open(filename4, 'r') as file_object:
            for line in file_object:
                print(line.rstrip())        
    except FileNotFoundError:
        print("The file does not exist.")

def main():
    writePres()
    appendPres()
    readFile()

main()