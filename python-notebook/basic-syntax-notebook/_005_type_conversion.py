# You can use various type conversion functions to convert from one type to another
print("Original: ", (10 / 3), "Type: ", type(10 / 3), "After Conversion: ", int(10 / 3), "Type: ", type(int(10 / 3)))

# Note that when changing the type we're truncating the data and not rounding the data
print(int(12.945)) # This will return 12 not 13


# Other converters are
# int()
# float()
# str()

# In order to get user input we can use the in-built function input().
# But it's return type is string.

x = input("Enter any value: ")
y = input("Enter any value: ")

print(x + y) # This will concatinate the numbers.

print(int(x) + int(y))

# If you enter the floating point as input, then converting it to int will throw an error
# int(input(5.5)) will throw an error
# Instead use float(input(5.5))

a = input("Enter floating: ")

converted = float(a)
z = int(converted)
print("Type should be int: ", type(z), "Value: ", z)
