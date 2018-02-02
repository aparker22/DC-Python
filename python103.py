#Exercise 1
day = int(raw_input('Day (0-6)?  '))
daysOfTheWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

print daysOfTheWeek[day]

#Exercise 2
day1 = int(raw_input('Day (0-6)?  '))

if 0 < day1 < 6:
    print 'Go to work'
else:
    print 'Sleep in'

#Exercise 3
celcius = int(raw_input('Temperature in Celcius? ')) 
farenheit = celcius * (1.8) + 32
print '%d F' % farenheit

#Exercise 4
bill = int(raw_input('Total bill amount? '))
service = raw_input('Level of service? ')


if service == 'good':
    print 'Tip Amount: $%.2f' % (bill * 0.20)
    print 'Total amount: $%.2f' % ((bill * 0.20) + bill)
elif service == 'fair':
    print 'Tip Amount: $%.2f' % (bill * 0.15)
    print 'Total amount: $%.2f' % ((bill * 0.15) + bill)
else:
    print 'Tip Amount: $%.2f' % (bill * 0.10)
    print 'Total amount: $%.2f' % ((bill * 0.10) + bill)

#Exercise 5

split1 = int(raw_input('Split how many ways? '))


if service == 'good':
    print 'Tip Amount: $%.2f' % (bill * 0.20)
    print 'Total amount: $%.2f' % ((bill * 0.20) + bill)
    print 'Amount per person: $%.2f' % (((bill * 0.20) + bill) / 5)   
elif service == 'fair':
    print 'Tip Amount: $%.2f' % (bill * 0.15)
    print 'Total amount: $%.2f' % ((bill * 0.15) + bill)
    print 'Amount per person: $%.2f' % (((bill * 0.15) + bill) / 5)
else:
    print 'Tip Amount: $%.2f' % (bill * 0.10)
    print 'Total amount: $%.2f' % ((bill * 0.10) + bill)
    print 'Amount per person: $%.2f' % (((bill * 0.10) + bill) / 5)
