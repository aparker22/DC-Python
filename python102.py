#Exercise 1
name = raw_input('What is your name?  ')
print "Hello, %s!" % name

#Exercise 2
upper_case = name.upper()
length = len(name)
length1 = str(length)
print "HELLO AGAIN, %s!" % upper_case
print "YOUR NAME HAS " + length1 + " CHARACTERS IN IT!"

#Exercise 3
print """Please fill in the blanks below:
____(name)____'s favorite subject in school is ____(subject)____."""

name1 = raw_input('What is your name? ')
subject1 = raw_input('What is your favorite subject? ')
subject2 = subject1.lower()

print "%s's favorite subject in school is %s." % (name1, subject2)


