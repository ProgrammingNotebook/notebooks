# A list is an ordered collection of values.
# Lists and strings — and other collections that maintain the order of their items — are called sequences.

#---------------------
# Creating a new list
#---------------------
fruits = ['Apple', 'Banana', 'Orange']
prices = [40, 34.12, 25]

# You can also create a nested list too.
names = [['Avatar', 'Avtaar', 'Avataar'], (2010, 2022), 'James Cameron']

# Empty list is also a thing
story_characters = []

#--------------------
# Accessing elements
#--------------------

print('Director:', names[2])

# To display all the elements in the list you can use make of the loop

for i in [0, 1, 2]:
    print(fruits[i])

# This can be done better

for price in prices:
    print(price)

# You can also make use of the length function to get the length of the list
# and can use it along with the range function

games = ['Street Fighter', "Mario", "Horizon"]

length = len(games)

for i in range(length):
    print(games[i])

#-----------------
# List Operations
#-----------------

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

# We can concat two lists into one using the '+' operator
c = a + b

print(c)

# We can multiply the list too by using the '*' operator
print(a * 2)    # Results in [1, 2, 3, 4, 1, 2, 3, 4]

#-------------------
# Lists are Mutable
#-------------------

fruits[0] = 'Pear'  # This will modify the first element of the list and replace with the 'Pear'
print(fruits)

# There are following operations we can perform
# Adding elements
# Modify elements
# Delete elements

# Adding to empty list
story_characters.append('Hodor')
print(story_characters)

#-------------------------------------------------------------------------------
# You can only modify what's present in the list.
# You can't perform this operation
# story_characters[1] = 'Grey', coz there is no element at index 1, so this will
# cause an error
#-------------------------------------------------------------------------------

# But you can modify what's present
story_characters[0] = 'Grey'
print(story_characters)

# 1. Adding elements

x_men = []

# - Adding to empty list
x_men = ['Jean Grey']
print(x_men)

# - Adding to end
x_men.append('Professor')
print(x_men)

# - Adding at the start: You need to make use of the slice operation
x_men[0:0] = ['Wolverine']
print(x_men)

# - What will happen if I add new character to slice off others
x_men[0:] = ['Saber Tooth']
print(x_men)    # Yes this will delete all other elemets and keep only one at index 0


# 2. Deleting
thor_universe = ['Thor', 'Loki', 'Odin']
print(thor_universe)

# - Delete single element from the list
del thor_universe[1]
print(thor_universe)    # This will delete 2nd element i.e Loki from the list

# - Deleting using the slice
del thor_universe[1:5]
print(thor_universe)    # This will delete all elements after 1st, won't throw error for index unbound

#------------------------------
# Reference operator in Python
#------------------------------

# Keyword is known as 'is'

name = "Gagandeep"
alias = "Gagandeep"

print(name is alias)    # This is true coz in Python also strings are not created again.

# For list this can be different
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)       # True
print(a is b)       # False

x = ['a', 'b', 'c']
y = x

print(x == y)       # True
print(x is y)       # True

#---------------
# Cloning lists
#---------------

# What if we don't want to copy the reference of a list but a new list out of
# the older one, we can make use of cloning the list

z = [1, 2, 3, 4, 5]
w = z[:]

print(w)
print(w == z)       # True
print(w is z)       # False

#-----------------------
# Enumeration in Python
#-----------------------

# With lists we can use the enumeration function whenever we're in search of
# index also along with the value of the list

for (i, val) in enumerate(z):
    print(i, val)

#-----------------------------------------------------------------
# NOTE:
#   Python language is a pass by reference and not pass by value.
#-----------------------------------------------------------------

#-----------------
# Methods in List
#-----------------

# 1. append() - Add element to the end of the list
chess = []
chess.append('Rook')
chess.append('Horse')
chess.append('Queen')

print(chess)

# 2. insert() - Add an element at a defined index. Pushes other elements to back

chess.insert(0, 'Pawn')
print(chess)

# 3. count(x) - How many times is x present in the list.
# 4. extend([]) - Appends the passed list to the end of the existing list.
# 5. index(x) - Find the index of the element x's first occurrence.
# 6. reverse() - Reverses the list.
# 7. sort() - Sorts in the descending order.
# 8. split() - Splits the string to a list.
# 9. split('x') - Splits the string using the token x.

name = "My name is Singh, Gagandeep Singh"
name_list = name.split()
print(name_list)

name_joined = "_".join(name_list)
print(name_joined)

# Splitting string into character list
friend = 'Ramandeep'
x = list(friend)
print(x)



#----------
# Exercise
#----------
print(list(range(10, 0, -2)))
