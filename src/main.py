import json
import random
import string

def get_non_empty_input(prompt):
    response = input(prompt).strip()
    if len(response) == 0 or response == "":
        print("Cannot be empty..")
        return get_non_empty_input(prompt)

    return response

def put_password(data, identifier, username = None):
    password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(9, 13)))
    print("Your", end=" ")
    if not username:
        print("new", end=" ")
        data[identifier]["password"] = password
    else:
        data[identifier] = {
            "username": username,
            "password": password
        }

    print(f"password is '{password}'")

def main():
    data = {}

    while True:
        print()
        print("1) Add/Set Login")
        print("2) Delete Login")
        print("3) View Logins")
        print("*) Exit")

        print()
        option = input("Please select an option: ")

        if len(option) > 0 and option in "123":
            if option in "12":
                identifier = get_non_empty_input("Please enter your login identifier: ")

                if option == "1":
                    if identifier in data:
                        replace = input("Exists.. replace (y/N)? ").lower() == "y"
                        if replace:
                            put_password(data, identifier)

                    else:
                        username = get_non_empty_input("Please enter your username: ")
                        put_password(data, identifier, username)
                else:
                    if identifier in data:
                        del data[identifier]
                    else:
                        print("Does not exist..") # todo: something more
            else:
                print(json.dumps(data, indent=4))
        else:
            return

if __name__ == "__main__":
    main()