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

def sortable_first(contact):
    return contact.first
def sortable_last(contact):
    return contact.last
def sortable_phone(contact):
    return contact.phone



sorted_phonebook_first = sorted(phone_book, key=sortable_first)
sorted_phonebook_last = sorted(phone_book, key=sortable_last)
sorted_phonebook_phone = sorted(phone_book, key=sortable_phone)

def command_1(): 
    prompt_name = raw_input('Name?  ')
    for entry in phone_book:
        if entry.first == prompt_name:
            print '%s %s: %s' % (entry.first, entry.last, entry.phone)
            break

def command_2():
    prompt_new_name = raw_input('What is the first name?  ')
    prompt_new_name1 = raw_input('What is the last name?  ')
    prompt_new_number = raw_input('What is the new number?  ')
    prompt_new_name = Contact(prompt_new_name, prompt_new_name1, prompt_new_number)
    prompt_new_name.add()
    import pickle
    saved_file = open('phone_book.pickle', 'w')
    pickle.dump(phone_book, saved_file)
    saved_file.close()
    print phone_book


def command_3():
    prompt_deleted = raw_input('Which entry do you want to delete?  ')
    for entry in phone_book:
        if entry.first == prompt_deleted:
            phone_book.remove(entry)
            break

def command_4():
    sort_answer = int(raw_input("How would you like to sort? Enter 1 for first name, 2 for last name, or 3 for phone number:  "))
    while sort_answer < 4:
        if sort_answer == 1:
            print sorted_phonebook_first
            break
        if sort_answer == 2:
            print sorted_phonebook_last
            break
        if sort_answer == 3:
            print sorted_phonebook_phone

    else:
        exit()
        


           
def save():                                     #This is the function for option 5
    import pickle
    saved_file = open('phone_book.pickle', 'w')   #saved_file is a file name I created, phone_book is the name of my list
    pickle.dump(phone_book, saved_file)           #used same variables as the preceeding line
    saved_file.close()                             #the file phone_book.pickle actually saves in my directory
    print phone_book

def restore():
    global phone_book                                  #This is the function for option 6
    import pickle                                       #I had to add the word "global" in front of my list to make it the same variable as the one outside the function
    restored_file = open('phone_book.pickle', 'r')    #restored_file is a filename I created
    phone_book = pickle.load(restored_file)             #again used the name of my list, phone_book

def command_rules(prompt):
    while prompt in command_list:
        start()
        prompt = int(raw_input('What do you want to do (1-7)?  '))
        if prompt == 1:
            command_1()
            break
        if prompt == 2:
            command_2()
            break
        if prompt == 3:
            command_3()
            break
        if prompt == 4:
            command_4()
            break
        if prompt == 5:
            save()
            break
        if prompt == 6:
            restore()
            break
        if prompt == 7:
            quit_answer = raw_input('Would you like to quit? Y or N ')
            if quit_answer == 'N' or quit_answer == 'n':
                break
            elif quit_answer == 'Y' or quit_answer == 'y':
                print 'Thank you! Goodbye! '
                exit()
            else:
                quit_answer = raw_input('Would you like to quit? Y or N ')
                break
                

            
while prompt in command_list:
    command_rules(prompt)






    
        




