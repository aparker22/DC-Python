# Sum the numbers

numbers = [4, 7, 10, 5]

sum_numbers = 0

for number in numbers:
    sum_numbers += number

print sum_numbers
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print largest
print max(numbers)

smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
print smallest
print min(numbers)

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
print evens

positives = []

for number in numbers:
     if number > 0 :
         positives.append(number)
print positives

#Multiply a list

# Multiply Vectors

