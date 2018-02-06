title = 'Electronic Phone Book'
command1 = '1. Look up an entry'
command2 = '2. Set an entry'
command3 = '3. Delete an entry'
command4 = '4. List all entries'
command5 = '5. Quit'

print title
print """
%s
%s
%s
%s
%s
""" % (command1, command2, command3, command4, command5)



prompt1 = int(raw_input('What do you want to do (1-5)?  '))


contacts = {
    'melissa': {'Name': 'Melissa', 'Phone': '5'},
    'igor': {'Name': 'Igor', 'Phone': 1},
    'jazz': {'Name': 'Jazz', 'Phone': 3},
    'ashley': {'Name': 'Ashley', 'Phone': 2},
    'calli': {'Name': 'Calli', 'Phone': 4},
    'ava': {'Name': 'Ava', 'Phone': 6}
}


#This code calls the phone number for a name entered and it works!!

def look_up(contact_name):   
    return contacts[contact_name]['Phone']

#This sets up a new contact with phone number and it works!!

def set_up(new_name, new_number):
    contacts[new_name]= {'Name': new_name, 'Phone': new_number}
    return contacts[new_name]

#This deletes an entry, I think it works...
def delete_entry(entry):
    return contacts.pop(entry)

def sorting_name(c):
    return c['Name']

def sorting_number(c):
    return c['Phone']

def sorting(x):
    contacts1 = [
    {'Name': 'Melissa', 'Phone': 5},
    {'Name': 'Igor', 'Phone': 1},
    {'Name': 'Jazz', 'Phone': 3},
    {'Name': 'Ashley', 'Phone': 2},
    {'Name': 'Calli', 'Phone': 4},
    {'Name': 'Ava', 'Phone': 6}
]
    while x == 'Y':
        sort_style1 = raw_input('Which variable would you like to sort by?  ')
        if sort_style1 == 'Name' or 'name':
            print sorted(contacts1, key=sorting_name)
            break
        elif sort_style1 == 'Number' or 'number':
            print sorted(contacts1, key=sorting_number)
            break
        else:
            exit()



command_list = [1, 2, 3, 4, 5]



def command_rules(prompt):
    while prompt in command_list:
        prompt = int(raw_input('What do you want to do (1-5)?  '))
        if prompt == 1:
            prompt_name = raw_input('Name?  ')
            print look_up(prompt_name)
            break
        if prompt == 2:
            prompt_new_name = raw_input('What is the new name?  ')
            prompt_new_number = raw_input('What is the new number?  ')
            print set_up(prompt_new_name, prompt_new_number)
            break
        if prompt == 3:
            prompt_deleted = raw_input('Which entry do you want to delete?  ')
            print delete_entry(prompt_deleted)
            break
        if prompt == 4:
            sort_answer = raw_input('Would you like to sort: Y or N? ')
            if sort_answer == 'Y':
                sorting(sort_answer)
            elif sort_answer == 'N':
                    print contacts
            else:
                break
        if prompt == 5:
            quit_answer = raw_input('Would you like to quit? Y or N ')
            if quit_answer != 'Y' and quit_answer != 'N':
                quit_answer = raw_input('Would you like to quit? Y or N ')
            elif quit_answer == 'N':
                break
            else:
                print 'Thank you! Goodbye! '
                exit()
                

            
while prompt1 in command_list:
    command_rules(prompt1)





    
        




