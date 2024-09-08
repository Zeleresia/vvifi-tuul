import itertools
import random
import string

def generate_passwords(word, num_passwords):
    passwords = set()
    chars = string.ascii_letters + string.digits + string.punctuation
    while len(passwords) < num_passwords:
        # Generate random passwords with varying lengths
        length = random.randint(8, 16)
        additional_chars = ''.join(random.choices(chars, k=length - len(word)))
        position = random.randint(0, length - len(word))
        password = additional_chars[:position] + word + additional_chars[position:]
        passwords.add(password)
    
    # Save to file
    with open('passwords.txt', 'w') as file:
        for password in passwords:
            file.write(f'{password}\n')

generate_passwords('Nabila', 100000)