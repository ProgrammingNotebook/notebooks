# String is an object on Python

# Some of the available function for string are

greet = 'hello, world!'

print(greet.upper())
print(greet.capitalize())

my_name = 'gagandeep singh'
print(my_name.capitalize())
print(my_name.swapcase())

# String is simply an array in Python

name = 'Raman'
print(name[0])

print(list(enumerate(name)))


# To fetch the length of the string we can use the len() method

print(len(name))    # This will result in 5

length = len(name)
for i in range(length):
    print(name[i])

# We can also use the negative count to get the last character
print(my_name[-1])  # This will output `h`. from Singh


print("\n\n\n")
my_name_length = len(my_name)
count = my_name_length * -1

for x in range(-1, count - 1, -1):
    print(my_name[x])


dog_name = 'Bruno'

# Simplest of them is
for ch in dog_name:
    print(ch)


#-------
# Slice
#-------
movie = "Pirates' of' the' Caribbean"

print(movie[0:16])  # In slice n:m n = start from index, m = index - 1 so 14 means index 13

print(movie[7:16])  # This means from index 7 till index 15

print(movie[:10])   # This means from index 0 to 9

print(movie[:])     # This means whole string will be printed


# Way to check if the character belongs to that string.
print('x' in 'gagan')   # This will result in 'False'

# String has a format nethod

filler = 'Hi, my name is {0} and my age is {1}'.format('Gagan', 38)
print(filler)
