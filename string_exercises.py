# Uppercase

string1 = raw_input('Enter your text here. ')
upper_string1 = string1.upper()

print upper_string1

# Capitalize a string

string2 = raw_input('Enter your next text here. ')
capitalize_string2 = string2.capitalize()

print capitalize_string2

# Reverse a String

string3 = raw_input('Enter your next text here. ')

print string3[::-1]
print string3[0::2]

# Leetspeak

# Long-long Vowels

string4 = raw_input('Enter a word. ')

if 'oo' in string4:
    string4 = string4.replace('oo','ooooo')
    print string4
elif 'ee' in string4:
    string4 = string4.replace('ee','eeeee')
    print string4
else:
    print string4




