# SLICING LIST
#____________________________________________________________________________________________________________________________________________#
numlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] positive index
	  #[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1] negative index
print(numlist[-1]) # prints last number in list
print(numlist[0]) # prints first number in list

print(numlist[-3:-1]) # prints 7 and 8
print(numlist[0:2]) # prints 0 and 1

print(numlist[-3:]) # prints last three numbers
print(numlist[:3]) # prints first three numbers

print(numlist[::1]) # prints a copy of the list
print(numlist[::-1]) # prints a reverse copy of the list
print(numlist[::2]) # prints very other number of the list starting with 0
print(numlist[::-2]) # prints every other number of the list starting with 9
#____________________________________________________________________________________________________________________________________________#


# SLICING STRING
#____________________________________________________________________________________________________________________________________________#
url = "https://www.nasa.gov"

print(url[-4:]) # prints the top level domain
print(url[:8]) # prints https://
print(url[8:-4]) # prints url without https://
print(url[::-1]) # prints reverse string
#____________________________________________________________________________________________________________________________________________#