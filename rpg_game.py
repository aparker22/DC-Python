class Character(object):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def __repr__(self):
        return '%s' % self.name
    
    def alive(self):
        while self.health > 0:
            return self.health


class Hero(Character):
    def attack(self, enemy):
        enemy.health -= self.power
        print "You do %d damage to the dragon." % self.power
        if not enemy.alive():
            print "The %s is dead." % enemy
    
    def status(self):
        print "You have %d health and %d power." % (self.health, self.power)

    def add(self):
        hero_list.append(self)

class Villain(Character):
    def attack(self, hero):
        # Goblin attacks hero
        hero.health -= self.power
        print "The dragon does %d damage to you." % self.power
        if not hero.alive():
            print 'You are dead'


    def status(self):
        print "The dragon has %d health and %d power." % (self.health, self.power)

    def add(self):
        villain_list.append(self)
        

def flee(x, y):
    while x.alive():
        if x.health > 0:
            y.attack(x)
            break
        if x.health < 0:
            print 'You are dead'

def new_villain():
    new_character = raw_input('What is the name of the character?')
    new_health = int(raw_input('What is the new character\'s health? '))
    new_power = int(raw_input('What is the new character\'s power?  '))
    new_character = Villain(new_character, new_health, new_power)
    return new_character



viking = Hero('viking', 10, 5)
dragon = Villain('dragon', 6, 2)
hero_list = []
villain_list = []

viking.add()
dragon.add()
choice = 1

def main(x, y):
    while x.alive() and y.alive():
        x.status()
        y.status()
        print "What do you want to do?"
        print "1. fight %s" % y.name
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = int(raw_input())
        if input == 1:
            x.attack(y)
        elif input == 2:
            flee(x, y)
        elif input == 3:
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

def start():
    global choice
    while choice > 0 and choice < 4:
        print 'What do you want to do?'
        print '1. Play a game.'
        print '2. Add a villain.'
        print '3. Save game.'
        print '4. Load previous game.'
        print '>  '
        choice = int(raw_input())
        if choice == 1:
            hero_type = raw_input('Which hero character? ')
            villain_type = raw_input('Which bad guy? ')
            for i in hero_list:
                if i.name == hero_type:
                    x = i
            for j in villain_list:
                if j.name == villain_type:
                    y = j
            main(x, y)
            exit()
        elif choice == 2:
            new_villain()
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        else:
            print "Invalid input %r" % input
            break
       

start()
