# collect email from user
# split the email using @, the first part as the username
# second part will be removed as domain
# split domain using .

def main():
    print('Welcome to email slicer')
    print('')

    email_input = input('Enter your email address: ')

    (username , domain) = email_input.split('@')
    (domain , extension) = domain.split('.')

    print('Username: ', username)
    print('Domain: ', domain)
    print('Extension: ', extension)

while True:
    main()
