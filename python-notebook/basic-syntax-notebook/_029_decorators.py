# Everything in Python is an object, thus you can pass them to other functions
# Decorators are fucntions that take in fucntions and extend them.

def greet(func):
    def name():
        print("Hello, ")
        func()
    return name

def me():
    print('Gagan!')

greeeting_myself = greet(me)

print(greeeting_myself())


# What I thought of as an example, but with using the annotations or syntactic
# sugar

def manners(fun):
    def manner():
        fun()
        print('How are you?')
    return manner

@manners
def bar():
    print('Hello, Sir')

print(bar())


# You can extend the above function by simply adding params

def bar_manners(position):
    def greet(name):
        position(name)
        print('Howdy!')
    return greet

@bar_manners
def counter(name):
    print('Welcome back,', name)

print(counter('Gagandeep Singh'))


# Real world examples
# You can use them for logging purpose

def sum(a, b, c):
    return a + b + c

# What if in the above function I want to know the values passed and result

def log(fun):
    def display(a, b, c):
        print('Values passed:', a, b, c)
        response = fun(a, b, c)
        print('Result:', response)

    return display

@log
def add(a, b, c):
    return a + b + c

add(3, 6, 9)
