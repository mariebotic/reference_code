# STRING LISTS, TUPLES, & SETS
#_____________________________________________________________________________________________________________________________________________#
family_list = ["Marcos", "Antonio", "Mark", "Vanessa", "Alex"] # defines a list
family_tuple = ("Marcos", "Antonio", "Mark", "Vanessa", "Alex") # defines a tuple (unchanging)
family_set = {"Marcos", "Antonio", "Mark", "Vanessa", "Alex", "Rosie", "Chappie", "Tia"} # defines a set (randomized)
print(family_list)

family_list_length = len(family_list) # determines the length of the list
print(family_list_length)

marcos = family_list[0] # determines the variable at the set index of the list
print(marcos)

family_list.append("Reina") # appends the string to the end of the list
print(family_list)

family_list.insert(6, "Debbie") # insets the string to a specific location of the list
print(family_list)
 
animal_family_list = ["Rosie", "Chappie", "Tia"] # defines a list
animal_family_set = {"Rosie", "Chappie", "Tia","WallE"} # defines a set
family_list.insert(7, animal_family_list) # inserts list within the defined list at a specific index
print(family_list)

family_list.remove(animal_family_list) # undoes previous insert
family_list.extend(animal_family_list) # appends list to the defined list such that the new list is one uniform list
print(family_list)

tia = family_list.pop() # pops the string at the end of the list and catches it as a varible
print(tia)
print(family_list)
family_list.append(tia) # undoes previous pop
print(family_list)

family_list.reverse() # reverses the list
print(family_list)

family_list.sort() # sorts the list alphabetically
print(family_list)

family_list.sort(reverse = True) # sorts the list in reverse alphabetically
print(family_list)

print(f'The index of "Chappie" is {family_list.index("Chappie")}.') # determines the index of a string

print(f'Chappie is in the family: {"Chappie" in family_list}') # determines if the string is part of the list

for member in family_list: # prints every string in the list
	print(member)

for member, index in enumerate(family_list): # prints every string in the list as well as its index
	print(member, index)

for member, index in enumerate(family_list, start = 1): # prints every string in the list as well as its index starting with 1
	print(member, index)

family_list = ", ".join(family_list) # creates a string of comma seperated values
print(family_list)

family_list = family_list.split(", ") # turns a comma seperated values string into a list
print(family_list)
print(family_tuple)
print(family_set)

print(f"The list of family members and animal family members has {family_set.intersection(animal_family_set)} in common.") # determines the strings the first list has in common with the second list
print(f"The list of family members and animal family members does not have {family_set.difference(animal_family_set)} in common.") # determines the strings the first list does not have in common with the second list

union_set = family_set.union(animal_family_set) # joins two sets
print(union_set)

empty_list = list() # creates an empty list
empty_tuple = tuple() # creates an empty tuple
empty_set = set() # creates an empty set
#_____________________________________________________________________________________________________________________________________________#


# INTEGER LIST
#_____________________________________________________________________________________________________________________________________________#
age_list = [19, 17, 15] # defines a list
print(age_list)

age_list.sort() # sorts the list in ascending order
print(age_list)

print(f" The min age of the Miera children is {min(age_list)}.") # determines the min number in the set
print(f" The max age of the Miera children is {max(age_list)}.") # determines the max number in the set
print(f" The sum age of the Miera children is {sum(age_list)}.") # determines the sum of the numbers in the set
#_____________________________________________________________________________________________________________________________________________#