import os

profile = {}

if os.path.getsize('passwords.txt') != 0: # if the profile has been set up already, load in the username and password
    with open("passwords.txt") as f:
            (key, val) = f.readline().strip('\n').split()
            profile[key] = val


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
    
def main():
    if len(profile) == 0:
        print("It looks like you don't have a profile set up. Let's set one up for you!")
        while True:
            username = str(input("Please enter a username without any spaces: "))
            if not ' ' in username:
                break
        while True:
            password = str(input("Please enter a password without any spaces: "))
            if not ' ' in password:
                break
        # at this point, you have a valid username and password without spaces for the user 
        # now, add the username and password to the txt file as as key value pair
        passwords_file = open("passwords.txt", "a")
        passwords_file.write(username + " " + password)
        # now the username and the password are in the file for the user
    else: # grab the username and password for the user from the dictionary
        username = next(iter(profile))
        password = profile[username]
    
    while True:
        print()
        username_entry = str(input("Please enter your username to login: "))
        password_entry = str(input("Please enter your password to login: "))
        if username == username_entry and password == password_entry:
            break
        print("Incorrect username or password. Please try again.")

    while True:
        print()
        response = input(f"Welcome {username}! What would you like to do?:\nAdd A Password: [A]\nChange A Password: [C]\
        \nRemove A Password: [R]\nSELECT: ").lower()
        if response == 'a' or response == 'r' or response == 'c':
            break
        print("\n******************************")
        print("Please choose a valid choice.")
        print("******************************")
    

main()
    