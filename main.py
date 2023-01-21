import os
from os import path
import platform

# install and import paramiko at some point for remote access stuff
# tkinter modern for ui

username = None
password = None

websites = [] # list of website_logins items
# str : [{user, pass}, {user, pass}, {user, pass}]

# creates a folder for storing website login info if one is not already present
current_directory = os.getcwd()
path_to_websites = os.path.join(current_directory, r'website_details')
if not os.path.exists(path_to_websites):
   os.makedirs(path_to_websites)

class website_logins: # represents the all the different login info for a specific website
    def __init__(self, name: str):
        self.name = name
        self.accounts = {}

for file in os.listdir(path_to_websites):
    name = file[0 : -4]
    new_item = website_logins(name)
    with open(f"{path_to_websites}/{name}.txt") as f:
            lines = f.readlines()
            for line in lines:
                (u, p) = line.split()
                new_item.accounts[u] = p
    websites.append(new_item)
    # pick up here and load in the existing passwords

site_passwords = {}

if os.path.exists(f"{current_directory}/MasterLogin.txt"):
    with open("MasterLogin.txt") as f:
        (key, val) = f.readline().strip('\n').split()
        username = key
        password = val
else:
    open("MasterLogin.txt", "x")

def clear_screen():
    if platform.system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def change_master_login():
    global username, password
    entered_username = str(input("Please enter your current username: "))
    entered_password = str(input("Please enter your current password: "))
    if entered_username == username and entered_password == password:
        username = str(input("Please enter a new username to use: "))
        password = str(input("Please enter a new password to use: "))
        clear_screen()
        print("\nSuccessfully changed login information!")
    else:
        print("\nIncorrect username or password was entered. Please try again.\n")

def after_login_choices() -> str:
    while True:
        print()
        response = input("What would you like to do?:\nFetch A Password: [F]\nAdd A Password: [A]\nChange A Password: [C]\
        \nDelete A Password: [D]\nReset Master Login Information: [R]\nSave and Quit [S]\nSELECT: ").lower()
        if response == 'f' or response == 'a' or response == 'c' or response == 'd' or response == 'r' or response =='s':
            return response
        clear_screen()
        print("\n******************************")
        print("Please choose a valid choice.")
        print("******************************\n")
        print("\nHere are the sites you currently have login info for: ")
        for site in websites:
            print(site.name)

def main():
    print(r"""
    ███████╗ █████╗ ███████╗███████╗    ██████╗  █████╗ ███████╗███████╗
    ██╔════╝██╔══██╗██╔════╝██╔════╝    ██╔══██╗██╔══██╗██╔════╝██╔════╝
    ███████╗███████║█████╗  █████╗      ██████╔╝███████║███████╗███████╗
    ╚════██║██╔══██║██╔══╝  ██╔══╝      ██╔═══╝ ██╔══██║╚════██║╚════██║
    ███████║██║  ██║██║     ███████╗    ██║     ██║  ██║███████║███████║
    ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝""")
    print()

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
    
    clear_screen()
    print(f"Welcome {username}!\n")

    quit = False

    while quit == False:
        print("Here are the sites you currently have login info for: ")
        for site in websites:
            print(site.name)

        choice = after_login_choices() # returns either 'f' 'a' 'c' 'd' or 'r' for fetch password, add password, change password, delete password, or reset login 
        clear_screen()
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
                print("Here are the sites you currently have login info for: ")
                for site in websites:
                    print(site.name)
                site_choice = str(input("\nWhat site would you like to change the username and password for?: \n")).lower()
                site_logins = None
                found_site = False
                for site in websites:
                    if site.name == site_choice:
                        found_site = True
                        site_logins = site
                        break
                if found_site == True:
                    for u, p in site_logins.accounts.items():
                        print(f"Username: {u}   Password: {p}\n") # prints usernames and passwords for that site
                    old_username = str(input("What username's password would you like to change?: ")).lower()

                    for user in site_logins.accounts.keys():
                        if user == old_username:
                            new_password = str(input("What is the new password for that username?: "))
                            site_logins.accounts[old_username] = new_password
                            print(f"Successfully changed password for user: {old_username}!")
                            break 
                    else: 
                        print(f"{old_username} is not a valid username currently stored for {site_logins.name}.")
                else:
                    print(f"\nYou do not have any login information for {site_choice}")
                
        elif choice == 'a':
            valid_choices = True
            print("Here are the sites you currently have login info for: ")
            for site in websites:
                print(site.name)
            site_choice = str(input("\nWhat site would you like to add username and password for?: ")).lower()
            clear_screen()
            new_username = str(input("What username would you like to add?: ")).lower()
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
                clear_screen()
                print(f"\033[1mSuccessfully added login info for {new_username} in {site_choice}!\033[0m\n")
        
        elif choice == 'd':
            print("Here are the sites you currently have login info for: ")
            for site in websites:
                print(site.name)
            site_choice = str(input("\nWhat site would you like to delete logins for?: ")).lower()
            clear_screen()
            site_logins = None
            found_site = False
            for site in websites:
                if site.name == site_choice:
                    found_site = True
                    site_logins = site
                    break
            if found_site == True:
                print(f"Logins for {site_choice}:")
                for u, p in site_logins.accounts.items():
                    print(f"Username: {u}   Password: {p}") # prints usernames and passwords for that site
                print()
                reply = str(input("Would you like to delete all logins for this website or just one?:\nAll [A]\nOne [O]\nCHOICE: "))
                if reply.lower() == 'a':
                    websites.remove(site_logins)
                    print(f"Successfully removed all login items for {site_choice}")
                elif reply.lower() == 'o':
                    to_remove = str(input("\nType the username of the login you would like to remove: "))
                    if to_remove in site_logins.accounts.keys():
                        del site_logins.accounts[to_remove]
                        if len(site_logins.accounts) == 0:
                            websites.remove(site_logins)
                        clear_screen()
                        print(f"Successfully deleted the login for the username of \033[1m{to_remove}\033[0m in {site_choice}!\n")
                    else:
                        clear_screen()
                        print(f"Username {to_remove} does not exist in {site_logins.name}.\n")
                else: # must have entered an invalid option
                    clear_screen()
                    print("Invalid delete option entered.\n")
            else: # site was not found
                print(f"{site_choice} does not have any login info stored. Please enter a valid website to delete login info for.\n")
        
        else: # choice must be 's' for save and quit
            quit = True

            

    user_file = open("MasterLogin.txt", "w") # clears the current data in the MasterLogin.txt file before uploading new data
    user_file = open("MasterLogin.txt", "a")

    user_file.write(username + " " + password)

    # delete existing text files before uploading new logins in case a whole website's logins were deleted 
    for f in os.listdir(path_to_websites):
        os.remove(os.path.join(path_to_websites, f))
    
    # updates all the login information before exiting the program
    for website in websites:
        new_website_file = open(path_to_websites + f"/{website.name}.txt", "a")
        for u, p in website.accounts.items():
            new_website_file.write(u + " " + p + "\n")
    
    print(path_to_websites)

main()