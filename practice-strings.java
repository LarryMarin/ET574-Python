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
x = email.find("@")
print("User name: ", email[0:x])
y = email.rfind(".com")
print("Company name: ", email[x+1:y].upper())
