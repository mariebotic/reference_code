# STRINGS
#______________________________________________________________________________________________________________________________#
message = "Hello world"
print(message.lower())
print(message.upper())

message_doubleq = "Hello world" # double quotations message string
print(message_doubleq)

message_singleq = 'Hello world' # single quotations message string
print(message_singleq)

message_span = '''Hello
world''' # multiple lines message string
print(message_span)

message_length = len(message) # message string length including spaces
print(message_length)

hello = message[:5]	# access to "Hello" message string characters
print(hello)

world = message[6:]	# access to "World" message string characters
print(world)

l_count = message.count('l') # number of times "l" shows up in message string
print(l_count)

l_find = message.find('l') # first instance of "l" in message string
print(l_find)

new_message = message.replace("world", "Space") # replace "World" with "Space" in message string
print(new_message)

combined_message = message + ", " + new_message.lower()	# concatinates new message string with old message string
print(combined_message)

print(f'The message "{message}" and "{new_message}" are both forms of greetings.') # f string
#______________________________________________________________________________________________________________________________#


# STRING HELP
#______________________________________________________________________________________________________________________________#
print(dir(message)) # functions of message type 
print(help(str)) # funtions of string type with description
print(help(str.lower)) # function lower of string types with description
#______________________________________________________________________________________________________________________________#