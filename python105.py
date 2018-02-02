# Exercise 1 to 10
print 'Exercise 1'
for i in range(1, 11):
    print i

# Exercise n to m
print 'Exercise 2'
start = int(raw_input('Please enter a starting number. '))
end = int(raw_input('Please enter an ending number. '))

while start >= end:
    start = int(raw_input('Please enter a starting number. '))
    end = int(raw_input('Please enter an ending number. '))

print 'Start from: %d' % start
print 'End on: %d' % end

for i in range(start, (end + 1)):
    print i

# Exercise Odd Numbers
print 'Exercise 3'
for i in range(0, 11):
    if i % 2 != 0:
        print i

# Exercise How many coins?
print 'Exercise 4'
i = 0
print ' You have %d coins.' % i
answer = raw_input('Do you want another? ')

while answer == 'yes':
    print 'You have %d coins' % (i + 1)
    i += 1 
    answer = raw_input('Do you want another? ')
else:
    print 'Bye'

#Exercise Print a Square
print 'Exercise 5'

square = 5
for sides in range(square):
    print ('*' * 5)

# Exercise Print a Square II
print 'Exercise 6'

square2 = int(raw_input('How big is the square? '))
for sides in range(square2):
    print ('*' * square2)

# Exercise Print a Box

print 'Exercise 7'

width = int(raw_input('Width? '))
height = int(raw_input('Height? '))

print '*' * width
for i in range (height - 2):
    print ('*' + (' ' * (width - 2))+ '*')
print('*' * width)

# Exercise Print a Triangle
print 'Exercise 8'
stars = 1
triangle_height = 4
base = ((2 * triangle_height) - 1)

for i in range(stars, (triangle_height + 1)):
    print ((' ' * ((base - stars) / 2)) + ('*' * stars) + (' ' * ((base - stars) / 2)))
    stars += 2


# Exercise Print a Triangle II
print 'Exercise 9'

stars2 = 1
triangle_height2 = int(raw_input('What is the triangle height? '))
base2 = ((2 * triangle_height2) - 1)

for i in range (stars2, (triangle_height2 + 1)):
    print ((' ' * ((base2 - stars2) / 2)) + ('*' * stars2) + (' ' * ((base2 - stars2) / 2)))
    stars2 += 2 


