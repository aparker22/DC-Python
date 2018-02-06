class Person(object):
    def __init__(self, name, email, phone, friends, greeting_count):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = friends
        self.greeting_count = greeting_count

    def __repr__(self):
        return '%s %s %s' % (self.name, self.email, self.phone)
    
    def greet(self, other_person):
        print 'Hello %s, I am %s' % (other_person.name, self.name)

    def print_contact_info(self):
        print "%s's email: %s, %s's phone number: %s" % (self.name, self.email, self.name, self.phone)
    
    def add_friends(self, other_person):
        self.friends.append(other_person)
        print self.friends.__repr__()

    def num_friends(self):
        print len(self.friends)
    
    def object_name(self):
        return '%s %s %s' % (self.name, self.email, self.phone)
    





        
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948', [], 0)
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456', [], 0)

sonny.greet(jordan)
jordan.greet(sonny)
print 'Email: %s and Phone: %s' % (sonny.email, sonny.phone)
print 'Email: %s and Phone: %s' % (jordan.email, jordan.phone)

class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

van = Vehicle('Volkswagon', 'Routon', '2014')
suv = Vehicle('Toyota', '4Runner', '2007')
car = Vehicle('Volkswagon', 'Jetta', '2016')

print car.make, car.model, car.year

sonny.print_contact_info()

jordan.add_friends(sonny)
sonny.add_friends(jordan)

jordan.num_friends()

sonny.greet(jordan)
print sonny.object_name()

print sonny.__repr__()
