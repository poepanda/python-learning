# Let's play a bit with data types

# A string is a sequence of characters
a_string = 'This is a String!'
print('This is a string ', a_string)

# A integer is the whole number that 
# can be positive, negative or 0
a_integer = 13
print('This is an integer ', a_integer)

# A number with fractional part
# A real number that can be rational or irrational number
a_float = 13.0
print('A float', a_float)

# A list of values
a_list = ['I', 'am', 'a', 'list']
print('This is a list ', a_list) # This should print I
print('And the first item ', a_list[0])
a_list[0] = 'He'
a_list[1] = 'is'
print('And list can be changed ', a_list)

# A tuple
# A list of unchangable, immutable sequece of items
a_tuple = ('I', 'am', 'a', 'tuple')
print('A tuple ', a_tuple)

# A boolean with only 2 values: True of False
a_boolean = True
print('This is a boolean ', a_boolean)

# A dictionary is a list of key : values pairs
# The key is an immutable data type
# The value can be made of any dataTypes
a_dictionary = { 'wife': 'Su', 'girl fiend': 'Su', 'soul mate': 'Su' }
print('This is a dictionary ', a_dictionary)