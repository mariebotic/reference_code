# LIST COMPREHENSIONS
#_____________________________________________________________________________________________________________________________________________#
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # creates a list
print(nums)

nums_identical = [n for n in nums] # creates a list via list comprehension
print(nums_identical)

nums_squared = [n*n for n in nums] # creates a squared list via list comprehension
# used in place of list = map(lambda n: n*n, nums)
print(nums_squared)

nums_even = [n for n in nums if n%2 == 0] # creates an even list via lis comprehension
# used in place of list = filter(lambda n: n%2 == 0, nums)
print(nums_even)

nums_letter = [(letter, number) for letter in 'abc' for number in range(1, 3)]
print(f"There are {len(nums_letter)} combinations of abc and 123")
print(nums_letter)
#_____________________________________________________________________________________________________________________________________________#


# DICTIONARY COMPREHENSIONS
#_____________________________________________________________________________________________________________________________________________#
first_names = ["Vanessa", "Mark", "Marcos", "Antonio", "Alex", "Rosie"]
lastname = "Miera"
last_names = [lastname for i in range(len(first_names))]

dict_combined1 = {first:last for first, last in zip(first_names, last_names)}
print(dict_combined1)

dict_combined2 = {first:last for first, last in zip(first_names, last_names) if first != "Rosie"}
print(dict_combined2)
#_____________________________________________________________________________________________________________________________________________#


# SET COMPREHENSIONS
#_____________________________________________________________________________________________________________________________________________#
nums_set = {n for n in nums}
print(nums_set)
#_____________________________________________________________________________________________________________________________________________#