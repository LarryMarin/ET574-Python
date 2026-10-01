#1. Write an if-elif-else chain that determines a person’s stage of life.
# 1) Prompt and request an age from the console.
# 2) If the age is less than 0, print an error message, invalid age.
# 3) If the age is less than 2 years old, print a message, you’re a baby.
# 4) If the age is at least 2 years old but less than 4, print a message, you’re a toddler.
# 5) If the age is at least 4 years old but less than 13, print a message, you’re a kid.
# 6) If the age is at least 13 years old but less than 20, print a message, you’re a teenager.
# 7) If the age is at least 20 years old but less than 65, print a message, you’re an adult.
# 8) If the age is 65 or older, print a message, you’re an elder.

age = int(input("Please enter your age: "))

if age<0:
    print("Invalid age.")
elif age>=0 and age<2:
    print("You're a baby.")
elif age>=2 and age<4:
    print("You're a toddler.")
elif age>=4 and age<13:
    print("You're a kid.")
elif age>=13 and age<20:
    print("You're a teenager.")
elif age>=20 and age<65:
    print("You're an adult.")
else:
    print("You're an elder.")

#2. Implement the following to print a greeting to each user after they log in to a website.
# 1) Make a list of five usernnames, including the name “admin”.
# 2) Loop through the list and print a greeting to each user.
# 3) If the username is “admin”, print a special greeting, such as
# Hello Admin, would you like to see a status report?
# 4) Otherwise, print a generic greeting, such as
# Hello Eric, thank you for logging in again!
# *5) Implement if the list is empty by printing the message, We need to find some users

userNames = ["Tom", "Jerry", "Bob", "Donna", "Admin"]
# userNames = []
if userNames == []:
    print("We need to find some users!")
else:
    for names in userNames:
        if "admin" in names.lower():
            print(f"Hello {names}, would you like to see a status report?")
        else:
            print(f"Hello {names}, thank you for logging in again!")

#3. Implement the following to simulate how websites ensure that everyone has a unique username.
# 1) Make a list of five or more usernames called current_users.
# 2) Request an input of username.
# 3) Print a message, Sorry XXX, that name is taken and display the current user list if the input
# username has already been used.
# 4) Print a message, Great, XXX is still available and display the updated user list if the username has not
# been used.
# 5) Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' or ‘john’ should not
# be accepted

current_users = ['admin', 'tom', 'jerry', 'Dora', 'GEORGE']
user_name = input("Please enter a username: ")


if user_name.lower() in (name.lower() for name in current_users):
        print(f"Sorry {user_name}, that name is taken.")
        print(f"Current Users: {current_users}")
else:
        print(f"Great, {user_name} is available!")
        current_users.append(user_name)
        print(current_users)

#4. Implement the following to search for a letter in a list.
# 1) Create a list named vehicles of your choice such as car, Truck, boat, PLANE.
# 2) Request a user input for a search letter.
# 3) Use the decision structure in a for loop to search all the items which contain the input letter (ignoring
# case, case insensitive) in the list.
# 4) Print the item and its position in vehicles if it exists. Otherwise, print the statement indicating it does
# not contain the letter to search.
# 5) Print the error message if more than one letter is entered.

vehicles = ['car', 'Truck', 'boat', 'PLANE']

letter = input('Please enter a letter: ')

if len(letter) > 1:
     print("Invalid search letter.")
else:
     for item in vehicles:
          if letter.lower() in item.lower():
               print(f"{item} contains '{letter}' and it is in position {vehicles.index(item)}.")
          else:
               print(f"{item} does not contain {letter}.")

# 5. A - O, determine the output displayed by the lines of code where a, b, c = 2, 3, 0

#A print(a ** b == b ** a)
#prints false

#B print(a < b or b < a)
#prints true

#C print('dog' > 'cat' + 'mouse')
#prints true

#D print('Car' < 'Train')
#prints true

#E print((a == b) and ((a * a < b * b) or (b < a) and (2 * a < b)))
#prints false

#F print((a <= b) or ((a * a < b * b) or (b < a) and (2 * a < b)))
#prints true

#G print(not ((a < b) and (a < (b + a))))
#prints false

#H print("small" > "large" and (not c ))
#prints true

#I print(isinstance(c, int))
#prints true

#J print(isinstance(3.14, float))
#prints true

#K if (a < b < c):
#   b = c + a
# else:
#   b = c * a
#   print(b)
#prints 0

#L if ('A' in 'apple'):
# print("A as apple." )
# else:
# print('Oops, not there.')
#prints Opps, not there.

#M x = 6
# if (x < 0):
#   print('negative')
# else:
#   if (x == 0):
#       print('zero')
#   else:
#       print('positive')
#prints positive

#N n = 1
# if n <= 9:
#   print ("Less than ten.")
# elif n == 1:
#   print("Equal to one.")
#prints Less than ten.

#O let = input("Enter A, B or C: \n")
# let = let.upper()
# if (let == 'A'):
#   print('\nA, my name is Alice.')
# elif (let == 'B'):
#   print('\nTo be, or not to be.')
# elif (let == 'C'):
#   print('\nOh, say, can you see.')
# else:
#   print('\nInvalid letter.')
#depends on what the user inputs it will print one of these statements: (the users input will be changed to uppercase)
# A: A, my name is Alice.
# B: To be, or not to be.
# C: Oh, say, can you see.
# None of the letters listed: Invalid letter.
