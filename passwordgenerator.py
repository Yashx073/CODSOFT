import random
import string

length = int(input("Enter the length of the password: "))

lowercase_letters = string.ascii_lowercase

uppercase_letters = string.ascii_uppercase

digits = string.digits

special_characters = string.punctuation

all_characters = lowercase_letters + uppercase_letters + digits + special_characters

password = ''.join(random.choice(all_characters) for _ in range(length))

print(password)
