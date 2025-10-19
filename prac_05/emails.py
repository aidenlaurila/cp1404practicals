"""
Emails
Estimate: 20 minutes
Actual: 17 minutes
"""

def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").upper()
        if confirmation != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print("")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name_from_email(email):
    name = " ".join(email.split("@")[0].split(".")).title()
    return name

main()