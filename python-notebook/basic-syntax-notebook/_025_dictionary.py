#-----------------------
# Creating dictionaries
#-----------------------

# Creating empty

dic = {}

print(type(dic))


# Adding elements to the dictionary

dic['apple'] = 50
dic['banana'] = 60

print(dic)


# Accessing dictionary

print(dic['apple'])


# Deleting element from the dictionary

del dic['apple']

print(dic)

dic['pear'] = 30
dic['apple'] = 90
dic['kiwi'] = 120

print(dic)

keys_list = dic.keys()
print(type(keys_list))
print(keys_list)

value_list = list(dic.values())
print(type(value_list))
print(value_list)


# Creating dictionary directly

latest = {
    "name": "Gagandeep Singh",
    "age": 37,
}

print(latest['age'])
print(type(latest))
print(latest)
