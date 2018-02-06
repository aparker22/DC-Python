
#1. Write a program that prompts the user to enter 
# a file name, reads the contents of the file and prints it to the screen.
file = raw_input('Please enter a file name.  ')
file1 = open(file)
file_contents = file1.read()
print file_contents

# 2. Write a program that prompts the user to enter a file name, 
# then prompts the user to enter the contents of the file, and then saves the 
# content to the file.

file_name = raw_input('Please enter a file name.  ')
contents = raw_input('Please enter file contents:  ')
file_name1 = open(file_name, 'w')
file_name1.write(contents)
file_name1.close()
file_name2 = open(file_name)
file1_read = file_name2.read()
print file1_read

# 3. Write a program that prompts the user to enter a file name, then prints 
# the letter histogram and the word histogram of the contents of the file.

file_name3 = raw_input('Please enter a file name.  ')
file3 = open(file_name3)
contents3 = file3.read()
contents3_split = contents3.split()
letter_histogram = {}
word_histogram = {}

for char in contents3:
    if char in letter_histogram:
        letter_histogram[char] += 1
    else:
        letter_histogram[char] = 1

for word in contents3_split:
    if word in word_histogram:
        word_histogram[word] += 1
    else:
        word_histogram[word] = 1

print 'Letter Histogram: %s' % letter_histogram
print 'Word Histogram: %s' % word_histogram

