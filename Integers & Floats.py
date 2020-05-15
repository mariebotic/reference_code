# INTEGERS & FLOATS
#_________________________________________________________________________________________________________#
varint3 = 3 # define integer
print(varint3)

varint9 = 9 # define integer
print(varint9)

varfloat = 3.14 #define float
print(varfloat)

round_varfloat = round(varfloat, 1) # round variable to tens place
print(round_varfloat)

add = varint3 + varint9 # add integers
print(add)

subtract = varint9 - varint3 # subtract integers
print(subtract)

multiply = varint3 * varint9 # multiply integers
print(multiply)

divide = varint9 / varint3 # divide integers
print(divide)

power = varint3 ** 2 # set integer to the power of 2
print(power)

divisible = varint9 % varint3 # determine if integeger is divisible by integer
print(divisible)

order_operations1 = varint3 ** 2 * varint9 - varint9 # same order of operations
order_operations2 = varint3 ** 2 * (varint9 - varint9) # parenthesis take precedence 
print(order_operations1)
print(order_operations2)

varint = varint3 
varint += 6 # increments integer by + integer
varint -= 3 # increments integer by - integer
print(varint)

user = input("Enter a number: ")
print(f"The users input is equal to an int: {type(user) == int}") # user input is not an int
user = int(user) # change user input to int
print(f"The users input is equal to an int: {type(user) == int}") # user input is an int
#_________________________________________________________________________________________________________#