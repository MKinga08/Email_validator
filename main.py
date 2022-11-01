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


def special_char_validator(address):
    if "@" in address:
        username, domain = address.split("@")
        c, k = 0, 0
        s = r"[@_!#$%^&*()<>?/\}{~:|]"
        for i in range(len(username)):
            if username[i] in s:
                c += 1
        if c > 0:
            print("username should not contain any special characters")
        for j in range(len(domain)):
            if domain[j] in s:
                k += 1
        if k > 0:
            print("domain should not contain any special characters")
    return True


def empty_address(address):
    username, domain = address.split("@")
    if username == "":
        print("You must enter a username")
    if domain == "":
        print("You must enter a domain")


def main():
    while True:
        email = at_validator()
        empty_address(email)
        if special_char_validator(email):
            break


if __name__ == '__main__':
    main()
