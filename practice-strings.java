#Larry Marin

#1

greet = "welcome to a new semester!"
print(greet.capitalize())

first = input("First Name: ")
last = input("Last Name: ")
name = first + " " + last
print(name.title())
class1 = "et574"
class2 = "et506"
class3 = "et725"
courses = class1 + "\t" + class2 + "\t" + class3
print(courses.upper())

#2 Using String and Slicing Methods
email = "mjordan@nba.com"
print(email[::1])
x = email.find("mjordan")
print("User name: ", email[::x])
