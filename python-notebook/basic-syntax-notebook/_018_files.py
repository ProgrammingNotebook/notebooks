#------------------------------------------
# How to create a file and add text to it.
#------------------------------------------

# Opening a file creates a new handle, file is a handle here
file = open('test.txt', 'w')

# These statements will write text on a single line.
file.write('This is a test to understand,')
file.write(' the working of the files in')
file.write(' Python.')

file.close()


# In order to write to different lines

file = open('test.txt', 'w')

# These statements will write text on multiple line, because of escape character
# '\n'
file.write('This is a test to understand,\n')
file.write('the working of the files in\n')
file.write('Python.')

file.close()

#------------------------------------
# How to read file text line by line
#------------------------------------

handle = open('test.txt', 'r')

while True:
    line = handle.readline()
    if len(line) == 0:
        break
    print(line, end="")

handle.close()

#----------------------------
# Reading whole file at once
#----------------------------
handle = open('test.txt', 'r')

data = handle.read()
print(data)

handle.close()

#-------------------------------------------------------------------------------
# NOTE:
#   The above files are text files, we can also read binary files like images,
# zip file etc. All we need to do it instead of using 'r' and 'w', we need to
# use 'rb' and 'wb'.
#-------------------------------------------------------------------------------
