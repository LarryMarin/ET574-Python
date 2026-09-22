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
