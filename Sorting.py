# LIST SORTING
#_____________________________________________________________________________________________________________________________________________#
import random

numlist = [random.randrange(1, 11) for i in range(10)] # creates a list of 10 integers between 1 and 10 
print(numlist)

sorted_numlist = sorted(numlist) # creates a sorted list of the random list of integers starting with the lowest number
print(sorted_numlist)

reverse_numlist = sorted(numlist, reverse=True) # creates a reverse sorted list of the random list of integers starting with the highest number
print(reverse_numlist)

"""
numlist.sort() # sorts the random list of integers in place
print(numlist)

numlist.sort(reverse=True) # reverse sorts the random list of integers in place
print(numlist)
"""
#_____________________________________________________________________________________________________________________________________________#


# TUPLE SORTING
#_____________________________________________________________________________________________________________________________________________#
numtuple = tuple(numlist) # creates a tuple copy of the random list of integers
print(numtuple)

sorted_numtuple = sorted(numtuple) # creates a sorted list of the tuple copy
print(sorted_numtuple)
#_____________________________________________________________________________________________________________________________________________#


# DICTIONARY SORTING
#_____________________________________________________________________________________________________________________________________________#
dictionary = {'Vanessa': 'Miera', 'Mark': 'Miera', 'Marcos': 'Miera', 'Antonio': 'Miera', 'Alex': 'Miera'} # defines a dictionary
sorted_keys = sorted(dictionary) # creates a sorted list of keys based on the dictionary
print(sorted_keys)

reverse_keys = sorted(dictionary, reverse=True) # creates a reverse sorted list of keys based on the dictionary
print(reverse_keys)
#_____________________________________________________________________________________________________________________________________________#


# NEGATIVE NUM LIST SORTING
#_____________________________________________________________________________________________________________________________________________#
neg_numlist = [random.randrange(-10, 11) for i in range(10)] # creates a list of 10 integers between -10 and 10
print(neg_numlist)

sorted_neg_numlist = sorted(neg_numlist) # creates a sorted list of the random list of integers starting with the lowest number
print(sorted_neg_numlist)

sorted_abs_neg_numlist = sorted(neg_numlist, key=abs) # creates a sorted list of the random list of integers based on the numbers absolute value
print(sorted_abs_neg_numlist)
#_____________________________________________________________________________________________________________________________________________#