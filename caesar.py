string1 = raw_input('Please enter a sentence. ')


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capital_alphabet = []

for letter in alphabet:
    cap_letter = ''
    if letter in alphabet:
        cap_letter = letter.capitalize()
        capital_alphabet.append(cap_letter)
        
def cipher_key(string):
    cipher = ''
    
    for i in string:
        if i in alphabet or capital_alphabet:
            cipher += i
        elif i not in alphabet or capital_alphabet:
            cipher += ' '
    return cipher

print cipher_key(string1)