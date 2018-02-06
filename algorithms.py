# Algorithm 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

multiples = 0

for i in range(0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        multiples += i
     

print multiples

# ALgorithm 2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


ending_number = 4000000
a = 1
b = 2
fibonacci_sequence = [a, b]
i = 1

while b <= ending_number:
    b = fibonacci_sequence[i] + fibonacci_sequence[i-1]
    fibonacci_sequence.append(b)
    i +=1

print fibonacci_sequence

evens = []
for number in fibonacci_sequence:
    if number % 2 == 0:
        evens.append(number)

sum_fibonacci_sequence = 0

for number in evens:
    sum_fibonacci_sequence += number

print sum_fibonacci_sequence

# Option 3:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
from math import sqrt
first_number = 600851475143 #n
factor_list_1 = []

def factoring(big_number):
    root = sqrt(big_number)
    max_number = int(root)
    factor_list = []    

    for i in range(2, max_number):
        if big_number % i == 0:
            factor_list.append(i)
            max_number = big_number / i
    return factor_list
        
    # def factoring2(factor_list):
    #     variable = max(factor_list)
    #     variable2 = min(factor_list)
    #     prime_list = []
    #     for i in factor_list:
    #         if i % variable2 != 0:
    #             prime_list.append(i)
    #     return prime_list
    

print factoring(first_number)

def factoring2(another_number):
    variable2 = factor_list[0]
    prime_list = []

    for i in factoring(first_number):
        if i % variable2 != 0:   #I want my code to cycle through multplying the list by other itemsin the list
            prime_list.append(i)
            variable2 += 1

# print prime_list




print factoring(13195)
print factoring2(factoring(13195))





    