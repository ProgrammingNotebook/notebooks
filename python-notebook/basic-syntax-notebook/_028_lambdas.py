# Lambdas are anaonymous functions

# Syntax: lambda arguments : expression

x = lambda a : a * 5
print(x(30))


# Lambda can have any number of arguments

a = lambda a, b : a * b
print(a(5, 6))


# Lambdas can be used inside functions to reveal it's true power

def calculator(basic, other):
    return lambda bonus : (basic + other) * bonus

bonus = calculator(100, 200)
print(bonus(130))


# Using lambdas directly
print((lambda x : x + 5)(2))


def increment():
    return lambda n : n + 1

counter = increment()

print(counter(1))
print(counter(5))


#------------------------
# Functions as arguments
#------------------------

# Using lambdas you can pass functions as an arguments

def calculator(func, a, b):
    return func(a, b)

def add(a, b):
    return a + b

# Passing the method reference here
print(calculator(add, 100, 500))

# Just playing, but this can also be done
print(calculator(lambda a, b: a * b, 13, 7))


#--------------------------------------------------------
# Using lambdas with built in functions: map(), filter()
#--------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

power = list(map(lambda x: x ** 2, numbers))
print(power)

# filter method
cords = [1, 2, 3, 4, 5, 6]
odd_one_out = list(filter(lambda x: x % 2 == 0, cords))
print(odd_one_out)
