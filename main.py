from operator import truediv
import os
from os import path
import platform

username = None
password = None

websites = [] # list of website_logins items
# str : [{user, pass}, {user, pass}, {user, pass}]

# creates a folder for storing website login info if one is not already present
current_directory = os.getcwd()
path_to_websites = os.path.join(current_directory, r'website_details')
if not os.path.exists(path_to_websites):
   os.makedirs(path_to_websites)

site_passwords = {}

class website_logins: # represents the all the different login info for a specific website
    def __init__(self, name: str):
        self.name = name
        self.accounts = {}
"""
def remove_password(site: str) -> bool:
    if site_passwords.pop(site.lower, -1) == -1:
        return False
    return True        
"""
if os.path.getsize('MasterLogin.txt') != 0: # if a profile has been set up already, load in the username and password for it
    with open("MasterLogin.txt") as f:
        (key, val) = f.readline().strip('\n').split()
        username = key
        password = val

def change_master_login():
    global username, password
    entered_username = str(input("Please enter your current username: "))
    entered_password = str(input("Please enter your current password: "))
    if entered_username == username and entered_password == password:
        username = str(input("Please enter a new username to use: "))
        password = str(input("Please enter a new password to use: "))
        if platform.system == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
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
        if platform.system == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
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
            entered_username = str(input("Please enter your username/email to login with: "))
            entered_password = str(input("Please enter the password to login: "))
            if entered_username == username and entered_password == password:
                break
            print("\nIncorrect username or password was entered.\n")
    
    print()
    print(f"Welcome {username}!")

    quit = False

    while quit == False:
        print("Here are the sites you currently have login info for: ")
        for site in websites:
            print(site.name)

        choice = after_login_choices() # returns either 'f' 'a' 'c' 'd' or 'r' for fetch password, add password, change password, delete password, or reset login 
        if platform.system == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        if choice == 'f':
            if len(websites) == 0:
                print("\nMust have login info for at least one website added to fetch.")
            else:
                site_logins = None
                site_choice = str(input("For which site do you want to access usernames and passwords for?: ")).lower()
                found_site = False
                for site in websites:
                    if site.name == site_choice:
                        found_site = True
                        site_logins = site
                        break
                if found_site == True:
                    for u, p in site_logins.accounts.items():
                        print(f"Username: {u}   Password: {p}") # prints usernames and passwords for that site
                    print()
                else: 
                    print("You do not currently have login info stored for that website.")
        elif choice == 'r':
            change_master_login()
        elif choice == 'c':
            if choice == 'c' and len(websites) == 0:
                print("\nMust have login info for at least one website added to change login information.")
            else:
                site_choice = str(input("What site would you like to change the username and password for?: ")).lower()
                site_logins = None
                found_site = False
                for site in websites:
                    if site.name == site_choice:
                        found_site = True
                        site_logins = site
                        break
                new_username = str(input("What username would you like to change?: ")).lower()
                new_password = str(input("What is the new password for that username?: "))
                
                
        elif choice == 'a':
            valid_choices = True
            site_choice = str(input("What site would you like to add/change username and password for?: ")).lower()
            new_username = str(input("What username would you like to add/change?: ")).lower()
            new_password = str(input("What is the new password for that username?: "))

            if ' ' in new_username or ' ' in new_password:
                print("Username cannot have spaces.")
                print("Password cannot have spaces.")
                valid_choices = False

            if valid_choices == True:   
                site_logins = None
                found_site = False
                for site in websites:
                    if site.name == site_choice:
                        found_site = True
                        site_logins = site
                        break
                if found_site == True: # if the site already has login info stored
                    site_logins.accounts[new_username] = new_password
                else: # create a new website_logins object for the login and add it to the list of known websites
                    new_website = website_logins(site_choice)
                    new_website.accounts[new_username] = new_password
                    websites.append(new_website)
                print(f"Successfully added/changed login info for {site_choice}!")
        
        elif choice == 'd':
            quit = True
        
        else: # choice must be 'q' for quit
            quit = True

            

    user_file = open("MasterLogin.txt", "w") # clears the current data in the MasterLogin.txt file before uploading new data
    user_file = open("MasterLogin.txt", "a")

    user_file.write(username + " " + password)
    
    # updates all the login information before exiting the program
    for website in websites:
        if path.exists(path_to_websites + f"/{website.name}.txt"): # if the file for that website already exists
            website_file = open(path_to_websites + f"/{website.name}.txt")
            website_file = open(path_to_websites + f"/{website.name}.txt")
            for u, p in website.accounts.items():
                website_file.write(u + " " + p + "\n")
        else:   # if the website doesn't already have a file of its own
            new_website_file = open(path_to_websites + f"/{website.name}.txt", "a")
            for u, p in website.accounts.items():
                new_website_file.write(u + " " + p + "\n")
    
    print(path_to_websites)

main()