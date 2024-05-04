import string
import random

characters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)

def generate_password():
    password_length = int(input("How many digits password you are looking for: "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate a password (Yes/No): ")

if option == "Yes".lower():
    generate_password()

elif option == "No".lower():
    print("Program Ended")
    quit()

else:
    print("Invalid input, pleasr enter (Yes/NO)")
    quit()

