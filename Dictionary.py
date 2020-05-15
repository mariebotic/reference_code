# DICTIONARIES
#_____________________________________________________________________________________________________________________________________________#
student = {"name": "Alexandria Miera", "age": 19, "courses": ["PH1120", "MA2051", "ECE2010"]} # defines a dictionary
print(student)
print(len(student)) # prints number of items present in dictionary

keys = student.keys() # creates a list of the keys defined in the dictionary
print(keys)
values = student.values() # creates a list of the values defined in the dictionary
print(values)
items = student.items() # creates a list of the items defined in the dictionary
print(items)

for keys, items in student.items(): # creates a loop that prints each item in a dictionary
	print(keys, items)


name = student["name"] # grabs the value under specified key
print(name)

age = student.get("age") # grabs the value under specified key
print(age)

student["graduation date"] = 2023 # appends a new item to the end of the dictionary
print(student)

student["name"] = "Alexandria Marie Miera" # updates the value defined by the specified key
print(student)

student.update({"university":"Worcester Polytechnic Institute", "degree":"ECE"}) # appends a dictionary to the main dictionary
print(student)

del student["university"] # deletes an item under specified key
print(student)

degree = student.pop("degree") # pops an item under specified key
print(degree)
#_____________________________________________________________________________________________________________________________________________#
