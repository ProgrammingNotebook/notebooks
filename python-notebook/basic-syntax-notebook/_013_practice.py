# 1. Write a function to count how many odd numbers are in the list.

def odd_number_counter(list):

    counter = 0
    for number in list:
        if number % 2 != 0:
            counter = counter + 1

    return counter

# print("Count: ", odd_number_counter([1, 34, 62, 7, 2, 845, 366, 436, 77]))

# 2. Sum up all the even numbers in a list.

def add_all_even_numbers(list):

    sum = 0
    for number in list:
        if number % 2 == 0:
            sum = sum + number
    return sum

#print("Sum: ", add_all_even_numbers([1, 34, 62, 7, 2, 845, 366, 436, 77]))

# 3. Sum up all the negative numbers in a list.

def add_all_odd_numbers(list):

    sum = 0
    for number in list:
        if number % 2 != 0:
            sum = sum + number
    return sum

# print("Sum: ", add_all_odd_numbers([1, 34, 62, 7, 2, 845, 366, 436, 77]))


# 4. Count how many words in a list have length 5.

def word_length_higher_than_five(list):

    count = 0
    for word in list:
        if len(word) > 5:
            count = count + 1;
    return count

# print("Count: ", word_length_higher_than_five(['This', 'chapter', 'showed',
# 'us', 'how', 'to','sum', 'a', 'list', 'of', 'items', 'and', 'how', 'to',
# 'count', 'items']))
