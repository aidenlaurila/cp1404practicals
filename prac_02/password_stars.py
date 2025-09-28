"""Password Program that gets user password and prints asteriks"""

MINIMUM_LENGTH = 7
def main():
    """Gets user password and censors it"""
    password = get_password()
    display_blurred_password(password)

def get_password():
    """Asks user for password until its length is valid"""
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f'Password must be at least {MINIMUM_LENGTH} characters long')
        password = input("Enter password: ")
    return password

def display_blurred_password(password):
    """Prints blurred password"""
    print(len(password) * '*')


main()