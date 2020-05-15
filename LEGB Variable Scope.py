# LEGB VARIABLE SCOPE
#____________________________________________________________________________________________________________________________________________#
x = "Global x" # creates a global variable


def outer(): # creates a global function variable outer
	# if global x needed to be changed within the local function, call "global x" meaning "Nested local" printed three times
	x = "Local x" # creates local variable


	def inner(): # creates a local function variable inner
		# if local x needed to be changed within the inner function, call "nonlocal x" meaning "Nested local" printed twice
		x = "Nested local x" # creates nested local variable
		print(x) # prints nested local x because found x in E
		# if print(x) was commented out, "Local x" would be printed twice

	inner() # runs inner
	print(x) # prints local x because found x in L

outer() # runs outer
print(x) # prints global x because there is no x found L, E


def min(): # creates a global function variable min
	min = "Overwritten built-in variable" # if min() function was used, error will occur
	print(min) # prints local min because min found in L
min() # runs min


def global_variable(x): # creates a global function variable global_variable
	print(x) # prints value passed in as x

inner("Local variable x") # passes in value for local variable x
#____________________________________________________________________________________________________________________________________________#