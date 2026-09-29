#1a. Print all the odd numbers from 1 to 9 inclusive in a list, odd_num
odd_num = [value for value in range(1,10,2)]
print(odd_num)

#1b.Make a list of the first 10 cubes.
# Use a for loop to print out the value of each cube in a new line (see output below)

cubes = [cube**3 for cube in range(1,11)]

for value in cubes:
    print(value)

#1c.Use a list comprehension to generate a list of the first 10 cubes.
# Use a for loop to print out the value of each cube in a row separated by a ‘|’ (see output below).

cubes2 = [cube**3 for cube in range(1,11)]

for value in cubes:
    print(value, end='|')

print('\n')
#2. List slicing.
# 1) Use a list comprehension to generate a list of all even numbers from 0 to 100 inclusive.
# 2) Use slicing to print the first five even numbers in the list.
# 3) Use slicing to print the last five even numbers in the list.
# 4) Use slicing and index method to print all list numbers between 44 and 88 inclusive

even_list = [nums for nums in range(0,101,2)]
print(even_list[:5])
print(even_list[-5:-1])
print(even_list[22:45])

#3. Lists, comprehensions, loops and slicing.
# 1) Create a list comprehension that generates the first 11 multiples of 4, starting from 0.
# 2) Print this list as displayed in the example output.
# 3) Create a second empty list.
# 4) Use a loop to insert all elements from the first list to the second list.
# Before storing into the new list, divide each copied element by 2.
# This results in a new list of all multiples of 2 from 0 to 10 inclusive.
# 5) Print the second list as displayed in the example output.
# 6) Use slicing to copy the second list to a new third list.
# 7) Use a loop to divide and store each element of the third list by 2.
# This will result in a list of the numbers 0 to 10 inclusive.
# 8) Print the third list as displayed in the example output

lst = [n*4 for n in range(0,11)]
print(lst)

lst2 = []

for index in lst:
    index = int(index/2)
    lst2.append(index)
print(lst2)

lst3 = lst2[:]

for index in lst3:
    index = int(index/2)
    lst3[index] = index
print(lst3)

#4 Implement the following using functions to create a list and produce a multiplication table:
# 1) Write a function create_range_list(n) that takes an integer n and returns a list of numbers
# from 1 to n inclusive.
# 2) Write a function print_multiplication_table(lst, num) that takes the list from step 1
# and an integer num, then uses a loop to compute and print the multiplication table of num.
# 3) In your main program, prompt the user to input a range value and a number, and call both functions.
# 4) Use exception handling (try / except) to validate invalid input (e.g., non-integers or negative
# values).

def create_range_list(n):
    n = n+1
    newList = [value for value in range(1,n)]
    return newList

def print_multiplcation_table(lst, num):
    for value in lst:
        print(value, '\t*\t', num, '\t=\t', value*num)

def main():
    try:
        x = int(input("Enter a range: "))
        y = int(input("Enter an integer: "))
        userList = create_range_list(x)
        print_multiplcation_table(userList, y)
    except ValueError:
        print("Invalid input.")

main()
