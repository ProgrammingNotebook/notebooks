# Set in Python are
# mutable,
# unordered,
# unique elements


# Creating an empty set

my_set = {1, 2, 3}

print(type(my_set))

print("\n\n")


# Operations on a Set

a = {1, 2, 4, 6, 8}
b = {1, 2, 3, 4, 5}

print("A: ", a)
print("B: ", b)

#-------------------------------------------------------
# 1. Union
# Common elments from the set will be copied only once.
#-------------------------------------------------------

u = a.union(b)

# or you can also use the | operator

un = a | b

print("a.union(b)", type(u), u)
print("a | b", type(un), un)

print("\n")


#------------------------------------
# 2. Intersection
# Common elments will only be copied
#------------------------------------


i = a.intersection(b)

# or you can also use the | operator

intsec = a & b

print("a.intersection(b)", type(i), i)
print("a & b", type(intsec), intsec)

print("\n")

#---------------------------------------------------------
# 1. Difference
# Common elements will be deleted from the caller element
#---------------------------------------------------------

# This is a - b, so all the b elements will be removed from a, thus common from
# the set will be deleted.
da = a.difference(b)
dia = a - b

db = b.difference(a)
dib = b - a

print("a.difference(b)", type(da), da)
print("a - b", type(dia), dia)

print("")

print("b.difference(a)", type(db), db)
print("b - a", type(dib), dib)

print("\n")
