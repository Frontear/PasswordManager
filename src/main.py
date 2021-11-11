import config

if __name__ == "__main__":
    while True:
        while len(key := input("Please enter your password: ")) == 0:
            print("Password cannot be empty.")

        if config.load(key):
            break

    while True:
        print("1) Add Login")
        print("2) Delete Login")
        print("3) View Logins")
        print("*) Save & Exit")
        print()

        choice = input("Enter your choice: ")

        if len(choice) > 0 and choice in "123":
            print("You chose {}".format(choice))
            print()
        else:
            print("Goodbye!")
            break