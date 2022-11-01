def get_users_input():
    address = input("What is your email address?")
    return address


def at_validator():
    while True:
        address = get_users_input()
        if address.count("@") == 1:
            return address
        elif address.count("@") > 1:
            print("You can only have one @ in your email address")
        else:
            print("You need to have one @ in your email address")


def empty_address(address):
    username, domain = address.split("@")
    if username == "":
        print("You must enter a username")
    if domain == "":
        print("You must enter a domain")


def special_char_validator(address):
    if "@" in address:
        username, domain = address.split("@")
        counter1, counter2 = 0, 0
        special_characters = r"[@_!#$%^&*()<>?/\}{~:|]"
        for i in range(len(username)):
            if username[i] in special_characters:
                counter1 += 1
        if counter1 > 0:
            print("username should not contain any special characters")
        for j in range(len(domain)):
            if domain[j] in special_characters:
                counter2 += 1
        if counter2 > 0:
            print("domain should not contain any special characters")
    return True


def domain_dot_validator(address):
    username, domain = address.split("@")
    if '.' in domain:
        beforedot, afterdot = domain.split(".")
        if beforedot == "upcmail":
            print("upcmail no longer exists :(")
        elif beforedot == "gmail" or beforedot == "hotmail" or beforedot == "freemail":
            if afterdot == "hu" or afterdot == "com" or afterdot == "de":
                print("Thank you for your subscription")
                return True
            else:
                print(f"{afterdot} is not a valid ending for an email address")
        else:
            print(f"{beforedot} is not a valid email address")
    else:
        print("You need to have a . in the domain part of you email address")


def main():
    while True:
        email = at_validator()
        empty_address(email)
        special_char_validator(email)
        if domain_dot_validator(email):
            break


if __name__ == '__main__':
    main()
