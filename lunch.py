class Restaurant(object):
    def __init__(self, number, name, choice):
        self.number = number
        self.name = name
        self.choice = choice
    
    def add(self):
        rest_list.append(self)
        return rest_list
    
    def __repr__(self):
        return '%s. %s' % (self.number, self.name)
    
rest_list = []

chipotle = Restaurant(1, 'Chipotle', 0)
farm_burger = Restaurant(2, 'Farm Burger', 0)
ru_susan = Restaurant(3, "Ru Susan's", 0)

chipotle.add()
farm_burger.add()
ru_susan.add()

choice = 0


def max_visits(x):
    for i in rest_list:
        if i.number == x:
            print 'You have visited %s times!' % i.choice
            if i.choice > 3:
                print 'Now choose another restauraunt'


def choose_restaurant():
    print rest_list
    global choice
    user_input = int(raw_input('Please choose a restaurant from the list:  '))
    for i in rest_list:
        if i.number == user_input:
            i.choice += 1
            if i.choice <= 3:
                print 'You chose %s' % i.name
                choice += 1
                max_visits(user_input)
                break
            if i.choice > 3:
                print 'You have reached max visits. Choose another restauraunt! '
                break



        
            

def print_list():
    for i in rest_list:
        print i.choice


for i in rest_list:
    global choice
    while choice < 5:
        choose_restaurant()



    

    

