first_name = raw_input('What is your first name?  ')
last_name = raw_input('%s! What is your last name?  ' % first_name)
full_name = '%s %s' % (first_name, last_name)

print "Hello " + full_name

length = len(full_name)
print length


