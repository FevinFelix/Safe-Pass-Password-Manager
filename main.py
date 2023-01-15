import os

username = None
password = None

site_passwords = {}

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

if os.path.getsize('MasterLogin.txt') != 0: # if a profile has been set up already, load in the username and password for it
    with open("MasterLogin.txt") as f:
        (key, val) = f.readline().strip('\n').split()
        username = key
        password = val

def change_master_login():
    global username, password
    entered_username = str(input("Please enter your current username "))
    entered_password = str(input("Please enter your current password: "))
    if entered_username == username and entered_password == password:
        username = str(input("Please enter a new username to use: "))
        password = str(input("Please enter a new password to use: "))
        print("\nSuccessfully changed login information!")
    else:
        print("\nIncorrect username or password was entered. Please try again.\n")

def after_login_choices() -> str:
    while True:
        print()
        response = input("What would you like to do?:\nFetch A Password: [F]\nAdd A Password: [A]\nChange A Password: [C]\
        \nDelete A Password: [D]\nReset Login Information: [R]\nSELECT: ").lower()
        if response == 'f' or response == 'a' or response == 'c' or response == 'd' or response == 'r':
            return response
        print("\n******************************")
        print("Please choose a valid choice.")
        print("******************************")

def main():
    global username, password
    if username == None:
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

    else: # if the profile was already created, prompt them to log in
        print("Welcome to your password manager!")
        while True:
            entered_username = str(input("Please enter a username/email to login with: "))
            entered_password = str(input("Please enter the password to login: "))
            if entered_username == username and entered_password == password:
                break
            print("\nIncorrect username or password was entered.\n")
    
    print()
    print(f"Welcome {username}!")

    quit = False

    while quit == False:
        print("Here are the sites you currently have passwords for: ")
        for site in site_passwords:
            print(site)

        choice = after_login_choices() # returns either 'f' 'a' 'c' 'd' or 'r' for fetch password, add password, change password, delete password, or reset login 
        
        if choice == 'f':
            if len(site_passwords) == 0:
                print("\nMust have at least one password added to fetch.")
            else:
                site_choice = None
                while True:
                    site_choice = str(input("For which site do you want to access passwords for?: "))
                    found_site = False
                    for site in site_passwords.keys():
                        if site == site_choice:
                            found_site == True
                            break
                    if found_site == True:
                        break
                    print("Please enter a site that you currently have a password stored for.")
                for site in site_passwords:
                    if site == site_choice:
                        for u, p in site_passwords.get(site_choice).items():   # looping through each username and password entry in that site (dictionary)
                            print(f"Username: {u}   Password: {p}") # prints usernames and passwords for that site
        elif choice == 'r':
            change_master_login()
        elif choice == 'a':
            quit = True




    """
    users_file = open("users.txt", "w") # clears the current data in the users.txt file before uploading data from users list
    users_file = open("users.txt", "a")
 
    for user in users: # saves the new data to text files before exiting password manager
        users_file.write(user.username + " " + user.password + "\n")
    """
main()