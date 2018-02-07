# # Exercise 1
# phonebook_dict = {
#     'Alice': '703-493-1834',
#     'Bob': '857-384-1234',
#     'Elizabeth': '484-584-2923'
# }

# print "Elizabeth's phone number is %r" % phonebook_dict['Elizabeth']

# phonebook_dict['Kareem'] = '938-489-1234'

# print "Phone book with Kareem: %r" % phonebook_dict

# phonebook_dict.pop('Alice')

# print "Phone book minus Alice: %r" % phonebook_dict

# phonebook_dict['Bob'] = '968-345-2345'

# print "Bob's new phone number is %r" % phonebook_dict['Bob']

# print phonebook_dict

# #Exercise 2

# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }

# print ramit['email']
# print ramit['interests'][0]

# print ramit['friends'][0]['email']
# print ramit['friends'][0]['interests'][1]

# # Exercise 3: Letter histogram

# user_word = raw_input('Please enter a word: ')
# histogram = {}

# for letter in user_word:
#     if letter in histogram:
#         histogram[letter] += 1
#     else:
#         histogram[letter] = 1

# print histogram

# # Exercise 4 Word Summary

# sentence = raw_input('Please enter a sentence. ')
# word_string = sentence.split()
# word_histogram = {}

# for word in word_string:
#     if word in word_histogram:
#         word_histogram[word] += 1
#     else:
#         word_histogram[word] = 1

# print word_histogram

# My own exercise
values = raw_input('Enter the names of your family: ')
values_split = values.split()
family_names = {}

for all_names in values_split:
    if all_names in family_names:
        family_names[all_names] += 1
    else:
        family_names[all_names] = 1
print family_names

Bonus Challenge - Histogram Tally

bonus_sentence = raw_input('Please enter a sentence: ')
split_sentence = bonus_sentence.split()
sentence_dictionary = {}

for words in split_sentence:
    if words in sentence_dictionary:
        sentence_dictionary[words] += 1
    else:
        sentence_dictionary[words] = 1

print sentence_dictionary

print max(sentence_dictionary)[1:3]









