def at_validator():
    while True:
        address = input("What is your email address?")
        if address.count("@") == 1:
            return address
        elif address.count("@") > 1:
            print("You can only have one @ in your email address")
        else:
            print("You need to have one @ in your email address")


def main():
    at_validator()


if __name__ == '__main__':
    main()
