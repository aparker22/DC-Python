title = 'Electronic Phone Book'
command1 = '1. Look up an entry'
command2 = '2. Set an entry'
command3 = '3. Delete an entry'
command4 = '4. List all entries'
command5 = '5. Save Entries'
command6 = '6. Restore saved entries'
command7 = '7. Quit'

print title
def start():
    print """
        %s
        %s
        %s
        %s
        %s
        %s
        %s
        """ % (command1, command2, command3, command4, command5, command6, command7)
        

prompt = 1
command_list = [1, 2, 3, 4, 5, 6, 7]
phone_book = []


class Contact(object):
    def __init__(self, first, last, phone):
        self.first = first
        self.last = last
        self.phone = phone
    
    def __repr__(self):
        return '%s %s %s' % (self.first, self.last, self.phone)

    def print_contact_info(self):
        print "Name: %s %s  Phone number: %s" % (self.first, self.last, self.phone)
    
    def add(self):
        phone_book.append(self)



melissa = Contact('Melissa', 'A', 5)
igor = Contact('Igor', 'B', 1)
jazz = Contact('Jazz', 'C', 3)
ashley = Contact('Ashley', 'D', 4)
calli = Contact('Calli', 'E', 2)
ava = Contact('Ava', 'F', 6)

melissa.add()
igor.add()
jazz.add()
ashley.add()
calli.add()
ava.add()


def look_up(): 
    prompt_name = raw_input('Name?  ')
    for entry in phone_book:
        if entry.first == prompt_name:
            print '%s %s: %s' % (entry.first, entry.last, entry.phone)
            break

def set_up(new_first, new_last, new_phone):
    new_first = Contact(new_first, new_last, new_phone)

def delete_entry():
    prompt_deleted = raw_input('Which entry do you want to delete?  ')
    for entry in phone_book:
        if entry.first == prompt_deleted:
            phone_book.remove(entry)
            break
def save():
    import pickle
    saved_file = open('phone_book.pickle', 'w')
    pickle.dump(phone_book, saved_file)
    saved_file.close()
    print phone_book

def restore():
    import pickle
    restored_file = open('phone_book.pickle', 'r')
    phone_book = pickle.load(restored_file)
    print phone_book

def command_rules(prompt):
    while prompt in command_list:
        start()
        prompt = int(raw_input('What do you want to do (1-7)?  '))
        if prompt == 1:
            look_up()
            break
        if prompt == 2:
            prompt_new_name = raw_input('What is the first name?  ')
            prompt_new_name1 = raw_input('What is the last name?  ')
            prompt_new_number = raw_input('What is the new number?  ')
            prompt_new_name = Contact(prompt_new_name, prompt_new_name1, prompt_new_number)
            prompt_new_name.add()
            print phone_book
            break
        if prompt == 3:
            delete_entry()
            break
        if prompt == 4:
            print phone_book
            break
        if prompt == 5:
            save()
            break
        if prompt == 6:
            restore()
            break
        if prompt == 7:
            quit_answer = raw_input('Would you like to quit? Y or N ')
            if quit_answer != 'Y' and quit_answer != 'N':
                quit_answer = raw_input('Would you like to quit? Y or N ')
            elif quit_answer == 'N':
                break
            else:
                print 'Thank you! Goodbye! '
                exit()
                

            
while prompt in command_list:
    command_rules(prompt)






    
        




