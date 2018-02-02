# Exercise 1 to 10
for i in range(1, 11):
    print i

# Exercise n to m

start = int(raw_input('Please enter a starting number 1-10. '))
end = int(raw_input('Please enter an ending number 11-20. '))

print 'Start from: %d' % start
print 'End on: %d' % end
for i in range(start, end):
    print i