import os

users = []
current_user = None

class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.password_pairs = {}

    def add_password(self, site: str, password: str) -> bool:
        if site.lower in self.password_pairs:
            return False
        else:
            self.password_pairs[site.lower] = password
            return True
    
    def remove_password(self, site: str) -> bool:
        if self.password_pairs.pop(site.lower, -1) == -1:
            return False
        return True        
    
    def change_password(self, site: str, new_password: str) -> bool:
        if site.lower in self.password_pairs:
            self.password_pairs.update({site, new_password})
            return True
        return False

if os.path.getsize('users.txt') != 0: # if a profile has been set up already, load in the usernames and passwords for each user
    with open("users.txt") as f:
            lines = f.readlines()
            for line in lines:
                (key, val) = line.strip('\n').split()
                users.append(User(key, val))

def add_user(username: str, password: str, users: list) -> bool:
    for user in users:
        if user.username == username:
            return False
    users.append(User(username, password))

def delete_user(username: str, users: list) -> bool:
    for user in users:
        if user.username == username:
            users.remove(user)
            return True
    return False

def after_login_choices() -> str:
    while True:
        print()
        response = input("What would you like to do?:\nAdd A Password: [A]\nChange A Password: [C]\
        \nRemove A Password: [R]\nSELECT: ").lower()
        if response == 'a' or response == 'r' or response == 'c':
            return response
        print("\n******************************")
        print("Please choose a valid choice.")
        print("******************************")

def before_login_choices() -> str:
    while True:
        print()
        response = input("What would you like to do?:\nAdd A User: [A]\nDelete A User: [D]\
        \nLogin As A User: [L]\nSELECT: ").lower()
        if response == 'a' or response == 'd' or response == 'l':
            return response
        print("\n******************************")
        print("Please choose a valid choice.")
        print("******************************")

def main():
    current_user = None
    if len(users) == 0:
        print("It looks like you don't have a profile set up. Let's set one up for you!")
        while True:
            username = str(input("Please enter a username without any spaces: "))
            if not ' ' in username:
                break
        while True:
            password = str(input("Please enter a password without any spaces: "))
            if not ' ' in password:
                break
        print("Successfully created the user profile.")
        # at this point, you have a valid username and password without spaces for the user 

        # also add the username and password to the users list as a new user
        add_user(username, password, users)

    else: # if there are already users available, show the active usernames that can be logged into
        print("Active usernames with passwords stored: ")
        for user in users:
            print(user.username)

    while current_user == None:
        before_login_choice = before_login_choices() # returns either 'a' 'd' or 'l' for add user, delete user, or login as a user
        print()
        if before_login_choice == 'a':
            username = None
            password = None
            while True: # gets a new username
                while True:
                    username = str(input("Please enter a new username without any spaces: "))
                    if not ' ' in username:
                        break
                check_valid = True
                for user in users:
                    if user.username == username:
                        check_valid = False
                        break
                if (check_valid == True):
                    break
                print("Username is already taken.")

            while True: # gets a new password
                password = str(input("Please enter a password without any spaces: "))
                if not ' ' in password:
                    break
            add_user(username, password, users)
        elif before_login_choice == 'd':
            while True:
                to_delete = str(input("Which user would you like to delete?: "))
                if(delete_user(to_delete, users) == True):
                    print("Successfully removed the user profile.")
                    break
                print("Please enter a valid user to delete.")
                print()
        else: # else, the user wants to login and chose 'l' 
            while True:
                username = None
                password = None
                while True: # gets a username to login to
                    username = str(input("Please enter a username to login with: "))
                    check_valid = False
                    for user in users:
                        if user.username == username:
                            check_valid = True
                    if check_valid == True:
                        break
                    print("Username does not exist.")

                valid_password = False
                password = str(input("Please enter the password to login: "))
                for user in users:
                    if user.username == username and user.password == password:
                        current_user = user
                        valid_password = True
                        break
                if valid_password == True:
                    break
                print("Incorrect password. Please try again.")
    
    print()
    print(f"Welcome {current_user.username}! Here are the sites you currently have passwords for:")
       

    after_login_choice = after_login_choices() # returns either 'a' 'c' or 'r' for add password, change password, or remove password

    users_file = open("users.txt", "w") # clears the current data in the users.txt file before uploading data from users list
    users_file = open("users.txt", "a")

    for user in users: # saves the new data to text files before exiting password manager
        users_file.write(user.username + " " + user.password + "\n")

main()
    