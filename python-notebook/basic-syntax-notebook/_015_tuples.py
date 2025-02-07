import math

# Tuples are immutable. They can't be changed once assigned.
# You can access the tuple values using the index.

me = ('Raman', 20, 'St. Joseph High School', 'Google')

print("I work at: ", me[3])

# Although you will not create a tuple with a single element, but if you do
# so you have to include a comma after that, otherwise it will be treated as
# a raw data type

numbers = (5,)
print('This is a tuple: ',type(numbers))


flag = (True)
print('This is not a tuple: ',type(flag))   # This will be <class 'bool'>

# You can't modify the existing tuple but you can create a new one.

me = me[:2] + ('GNPS',) + me[3:]
print("Tuple: ", me)

# When you need to assign various variables all at once, you can make use of
# the tuple assignment feature.

(name, age, high_school, works_at) = ('Aman', 22, 'GHPS', 'Amazon')

# Now you can use those variables separately
print(name, ' works at: ', works_at)


# This is interesting, swapping of two variables is so easy in Python
a = 10
b = 20

(a, b) = (b, a)

print('A: ', a, ' B: ', b)

# This is possible coz
# all the expressions on the right side are evaluated before any of the
# assignments. This feature makes tuple assignment quite versatile.


#--------------------------------------------------
# Values on the left needs to same as on the right
#--------------------------------------------------

# You can return tuple value from a function, this way you can return multiple
# values.
def circle(radius):

    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return (area, circumference)


(a, c) = circle(68)
print('Area: ', a, ' Circumference: ', c)

#---------------
# Heterogeneous
#---------------
# Don't be scared of the name, it's just a tuple containing other data type,
# including the tuple or the list also

actor = (('Hritik', 'Roshan'), (10, 'January', 1974),
    ['Kaho Na Pyaar Hai', 2000],
    ['Fiza', 2000],
    ['Mission Kashmir', 2000]
)

print('Actor: ', actor, '\n', 'Type: ', type(actor))



#----------
#----------
# Exercise
#----------
#----------

# 1. We’ve said nothing in this chapter about whether you can pass tuples as
# arguments to a function. Construct a small Python example to test whether
# this is possible, and write up your findings.

def rectangle(rectangle):

    (length, breadth) = rectangle
    area = length * breadth
    circumference = 2 * (length + breadth)

    return (area, circumference)


print('Rectangle: ', rectangle((10, 16)))
