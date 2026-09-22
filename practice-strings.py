# #Larry Marin

# #1

# greet = "welcome to a new semester!"
# print(greet.capitalize())

# first = input("First Name: ")
# last = input("Last Name: ")
# name = first + " " + last
# print(name.title())
# class1 = "et574"
# class2 = "et506"
# class3 = "et725"
# courses = class1 + "\t" + class2 + "\t" + class3
# print(courses.upper())

# #2 Using String and Slicing Methods
# email = "mjordan@nba.com"
# print(email[::1])
# x = email.find("@")
# print("User name: ", email[0:x])
# y = email.rfind(".com")
# print("Company name: ", email[x+1:y].upper())

#3 Using string indices.
# 1) Prompt and request an input string from the console.
# 2) Display the first and last letter of the string
# 3) Display the string in the reverse order

userString = input("Please enter a string: ")
print("Original Text: ", userString)
print("First Letter:", userString[0])
print("Last Letter:", userString[-1])
print("Reverse Order:", userString[::-1])

#4 Display the following triangle by using repetition of “ ” and “*” 

print(" "*7, "*", " "*7)
print(" "*6, "*"*3, " "*6)
print(" "*5, "*"*5, " "*5)
print(" "*4, "*"*7, " "*4)
print(" "*3, "*"*9, " "*3)
print(" "*2, "*"*11, " "*2)
print(" "*1, "*"*13, " "*1)
print(" "*0, "*"*15, " "*0)

#5a – i, identify the errors of each question in the comment and rewrite the statement in the correct syntax

#a) print(“Python”).Upper()
#.upper() is supposed to be lower case and inside the print statement after the quotation marks

print("Python".upper())

#b) Print(‘Say it ain’t so.’)
#Print needs to be lowercase and it needs to be in quotation marks not apostrophes 
print('Say it ain’t so.')

#c) print('*'*5 +Hotel+'*'*5)
#there needs to be commas where the plus' are and Hotel needs to be in quotations

print('*'*5, 'Hotel', '*'*5)

# #d) txt = "ET"
# class = 574
# print(txt+class)
#class needs to be renamed because it is using a special word and it needs to be changed into a String since it is currently a integer in order to concatonate it with txt
txt = "ET"
class1 = "574"
print(txt+class1)

# e) n = 1234
# print(n.find('2'))
#.find() is only for Strings so we have to turn n into a String
n = '1234'
print(n.find('2'))

# #f) num = 101
# print(num[0])
#This wants to print out the first index of num but since num is an integer it does not have an index. num needs to be changed into a String for this to work
num = '101'
print(num[0])

# #g) phoneNum = 718-710-4756
# print("QCC phone number is " + phoneNum + '.')
#phoneNum is not a String so - won't work. In order to print it out correctly it needs to be changed into a String
#also for consistency change the single '' to a double ""
phoneNum = "718-710-4756"
print("QCC phone number is " + phoneNum + ".")

# h) input = "Microsoft"
# print("Reversed Text:", input[-1:0])
#Splciing is done wrong. It cannot read from -1 to 0. For example t is -1 and M is -9. 0 does not work since we are going backwards.
#also input is a special word we should not use it

input1 = "Microsoft"
print("Reversed Text:", input1[::-1])

# i) age = input("Enter your age: ")
# print("Next year you will be " + (age+1))
#If we want age to be added by 1 we need to typecast the input to an int since input() without a typecasting is a String and numbers that are Strings cannot be added by 1 instead if concatonates it
#and we need to replace the + to a ,

age = int(input("Enter your age: "))
print("Next year you will be", (age+1))

x = '0123456789'
#print 574 using the index
print(x[5]+x[7]+x[4])
#print 456
print(x[4:7])
#using find is better and consistent
m = x.find('4')
n = x.find('7')
print(x[m:n])

