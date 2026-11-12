# 1) Create a dictionary, stuInfo with the keys name, gpa, and age. Give appropriate values for each key.
stuInfo = {"name": "John Smith", "gpa": 3.456, "age": 20}

# 2) Use a loop and the items() method to print all keys and values.
for key, value in stuInfo.items():
    print(key.title(), value)

# 3) Use the update() method to change the gpa to 4.0.
stuInfo.update({"gpa": 4.0})

# 4) Use a loop and the keys() method to print all keys and values
for key in stuInfo.keys():
    print(key.title(), stuInfo[key])

# 5) Add a key major with the value to the dictionary
stuInfo["major"] = "CSIS"

# 6) Use a loop and the values() method to print all values
for value in stuInfo.values():
    print(value, end = "|")
print()

# 7) Use two different ways to delete gpa and age in the dictionary.
del stuInfo["gpa"]
stuInfo.pop("age")

# 8) Print the updated dictionary.
print(stuInfo)

# 2. Displays a rank in the defined dictionary.
# 1) Create a dictionary, rank = {1:"Freshman", 2:"Sophmore", 3:"Junior", 4:"Senior"}
# 2) Prompt and request a user input.
# 3) Print the value of the matching key in the dictionary.
# 4) Print the error message if input is invalid

rank = {1:"Freshman", 2:"Sophmore", 3:"Junior", 4:"Senior"}

years = int(input("Enter the # of years in the school (1-4): "))

if years in rank:
    print(f"Years {years} = {rank[years]}")

else:
    print("Invalid years.")
