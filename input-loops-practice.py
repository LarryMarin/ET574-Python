# #1. For & While.
# # a) Use a for loop to print all the numbers are even from 1 to 100 inclusive.
# # b) Convert the for loop to a while loop

# for x in range(2,101, 2):
#     print(x, end = ' ')

# print()

# x = 2
# while x <=100:
#     print(x, end = ' ')
#     x+=2

# #2. For & While.
# # a) Use a for loop to print all the numbers are odd and multiples of 11 from 1 to 1000 inclusive.
# # b) Convert the for loop to a while loop
# print()

# for x in range(1,1001, 2):
#     if x%11==0:
#         print(x, end = ' ')
# print()

# x = 1

# while x <=1000:
#     if x%11==0:
#         print(x, end = ' ')
#     x+=2
# print()

# #3. Loop & Calculation.
# # a) Use a for loop to calculate and print the sum of all numbers between 1 to 100 inclusive

# sum = 0
# for x in range(1,101):
#     sum+=x
# print(sum)

# # b) Use a while loop to calculate and print the sum of all even numbers between 1 to 100 inclusive.

# sum = 0
# x = 1

# while x<=100:
#     if(x%2==0):
#         sum+=x
#     x+=1
# print(sum)

# #4. While & For.
# # a) Implement a while loop to print all the numbers from 9 to 1 inclusive.
# # b) Then display Happy New Year!
# # c) Convert the while loop to a for loop

# x = 9
# while x>=1:
#     print(x)
#     if x==1:
#         print('Happy New Year!')
#     x-=1

# for x in range(9,0,-1):
#     print(x)
#     if x==1:
#         print('Happy New Year!')

# #5. Define a function check_multiple_of_10() that:
# # a) Prompts the user to enter an integer.
# # b) Uses exception handling (try/except) to validate invalid input.
# # c) Prints whether the number is a multiple of 10 or not.
# # d) Call the function in your main program

# def check_multiple_of_10():
#     userIn = int(input("Please enter a integer: "))
#     try:
#         if userIn%10==0:
#             print(f"{userIn} is a multiple of 10.")
#         else:
#             print(f"{userIn} is not a multiple of 10.")
#     except ValueError:
#         print("Invalid Input.")
# check_multiple_of_10()
# #6. Update the above question with two functions:
# # a) Define a function get_valid_integer() that prompts the user for input, uses exception
# # handling (try/except) to validate invalid input, and returns the integer.
# # b) Define a function check_multiple_of_10(num) that takes an integer parameter and prints
# # whether it is a multiple of 10.
# # c) Call both functions in the main program

# def get_valid_integer():
#     userIn = int(input("Please enter an integer: "))
#     try:
#         return userIn
#     except ValueError:
#         print("Invalid Input.")

# def check_multiple_of_10(num):
#     if num%10==0:
#         print(f"{num} is a multiple of 10.")
#     else:
#         print(f"{num} is not a multiple of 10.")

# def main():
#     n = get_valid_integer()
#     check_multiple_of_10(n)
# main()

#7. Loop and Input.
# a) Create a function to request two integer inputs n1 and n2 with input validation
# (use exception handling to handle invalid input).
# b) Create another function that:
# 1) Uses a while loop to horizontally print numbers from n1 to n2 if n1 is smaller than n2 (increment by 1).
# 2) Uses a for loop to horizontally print numbers from n1 to n2 if n1 is greater than n2 (decrement by 1).
# 3) Prints a message "n1 = n2" if n1 is equal to n2.
# c) Call both functions in the main program.

# def user_input():
#     try:
#         n1 = int(input("Please enter the first integer n1: "))
#         n2 = int(input("Please enter the secoond integer n2: "))
#         return n1,n2
#     except ValueError:
#         print("Invalid input")

# def num_loop(n1,n2):
#     if(n1<n2):
#         while n1<=n2:
#             print(n1, end = ' ')
#             n1+=1
#     elif n1>n2:
#         for x in range(n1,n2-1, -1):
#             print(x)
#     elif n1==n2:
#         print("n1 == n2")

# def main():
#     n1, n2 = user_input()
#     num_loop(n1, n2)

# main()

#8. Sentinel While Loop.
# a) Create a function to request numbers from the console in a loop and insert them into a list.
# 1) The loop should continue until the user enters 0.
# 2) Use exception handling to validate invalid input.
# b) Create another function to:
# 1) Print all elements of the list.
# 2) Compute and print the sum of the list.
# 3) Compute and print the average of the list.
# c) Call both functions in the main program.

def request_nums():
    lst = []
    while True:
        try:

            x = float(input("Please enter a number (0 to exit): "))

            if x == 0:
                break

            if x.is_integer():
                lst.append(int(x))
            else:
                lst.append(x)
            
        except ValueError:
            print("Invalid Input. Please try again.")
        
    if len(lst) > 0:
        return lst
    else:
        return None

def print_lst(lst):
    if lst is None:
        return
    
    print(f"Sum = {sum(lst)}")
    print(f"Avg = {sum(lst)/len(lst):.2f}")
    print("Numbers entered: ")

    for x in range(len(lst)):
        print(lst[x], end = ' ')

def main():
    lst = request_nums()
    print_lst(lst)

main()
