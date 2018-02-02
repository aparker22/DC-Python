# Sum the numbers

numbers = [1, 2, 3, 4]
sum = 0

for number in numbers:
    sum += number
print sum

#function

def sum(x):
    total = 0
    for i in x:
        total += i
    return total

print sum([1, 2, 3, 4])
variable = [1, 2, 3, 4]
print sum(variable)

#Largest number

largest_number_list = [1, 2, 4, 6, 8]
largest = 0

for number in largest_number_list:
    if number > largest:
        largest = number
print largest

#Largest number function

def find_largest(y):
    largest1 = 0
    for number in y:
        if number > largest1:
            largest1 = number
    return largest1

print find_largest([1, 4, 7, 9, 3])

#smallest number

smallest_number_list = [1, 2, 4, 6, 8]
smallest = smallest_number_list[0]

for number in smallest_number_list:
    if number < smallest:
        smallest = number
print smallest

#Smallest number function

def find_smallest(y):
    smallest1 = y[0]
    for number in y:
        if number < smallest1:
            smallest1 = number
    return smallest1

print find_smallest([1, 4, 7, 9, 3])

#Even Numbers
even_number_list = [2, 5, 6, 9, 3, 4, 2]
evens = []

for i in even_number_list:
    if i % 2 == 0:
        evens.append(i)

print evens

#Even numbers function

def find_evens(nums):
    evens1 = []
    for number in nums:
        if number % 2 == 0:
            evens1.append(number)
    return evens1

print find_evens([1, 2, 3, 4])

#Positive numbers
list_of_pos = [1, 2, 3, -4, -5]
positives = []

for number in list_of_pos:
    if number >= 0:
        positives.append(number)

print positives

#Positive numbers function
def find_positives(x):
    positives1 = []
    for number in x:
        if number >= 0:
            positives1.append(number)
    return positives1

print find_positives([1, -1, 2, -2, 3, -3])

Positive Numbers II = same as above

#Multiply a list

list_of_multipliers = [1, 2, 3, 4]
factor = 2
multiplied = []

for number in list_of_multipliers:
    multiplied.append(number * factor)

print multiplied

#Multply a list function

def multiply_lists(x, y):
    multiplied1 = []
    for number in x:
        multiplied1.append(number * y)
    return multiplied1

print multiply_lists([1, 2, 3, 4], 2)

#Multiply vectors
vector1 = [1, 2, 3]
vector2 = [1, 2, 3]
new_vector = []

for i in range(0, len(vector1)):
    new_vector.append(vector1[i] * vector2[i])


print new_vector

def multiply_vectors(x, y):
    vector_lists = []
    for number in range(len(x)):
        vector_lists.append(x[number] * y[number])
    return vector_lists

print multiply_vectors([1, 2, 3], [1, 2, 3])

Adding Matrices

matrix1 = [
    [1, 3],
    [2, 4]
]

matrix2 = [
    [5, 2], 
    [1, 0]
]

height = len(matrix1)
width = len(matrix1[0])

result = []

for i in range(0, height):
    result.append([])
    for j in range(0, width):
        result[i].append(None)
print result

for i in range(0, height):
    for j in range(0, width):
        cell1 = matrix1[i][j]
        cell2 = matrix2[i][j]
        result[i][j] = cell1 + cell2
print result

# adding matrices function

def adding_matrices(x, y):
    height = len(x)
    width = len(x[0])
    result1 = []
    for i in range(0, height):
        result1.append([])
        for j in range(0, width):
            result1[i].append(None)

    for i in range(0, height):
        for j in range(0, width):
            cell3 = x[i][j]
            cell4 = y[i][j]
            result1[i][j] = cell3 + cell4
    return result1

new_matrix1 = [
    [1, 3],
    [2, 4]
]

new_matrix2 = [
    [5, 2], 
    [1, 0]
]

print adding_matrices(new_matrix1, new_matrix2)

#De-dup

string_list = ['Ashley', 'Brandon', 'Call', 'Ava', 'Ava', 'Kit', 'Kit']
deduped = []
for word in string_list:
    if word not in deduped:
        deduped.append(word)
print deduped
    
#De-duped function

def de_dup(x):
    new_list = []
    for word in x:
        if word not in new_list:
            new_list.append(word)
    return new_list

print de_dup(['one', 'two', 'three', 'three', 'four', 'four', 'five'])