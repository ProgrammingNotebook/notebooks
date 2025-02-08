try:
    num = 25 / 0
except:
    print("Can't divide by zero")


try:
    num = 25 / 0
except:
    raise ValueError("Can't divide by {0}".format(0))
