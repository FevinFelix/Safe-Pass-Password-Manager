import os

profile = None

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
    username = None
    password = None
    if os.path.getsize('passwords.txt') == 0:
        print("It looks like this is your first time using the password manager. Let's set up a profile for you!")
        while True:
            username = str(input("Please enter a username without any spaces: "))
            if not ' ' in username:
                break
        while True:
            password = str(input("Please enter a password without any spaces: "))
            if not ' ' in password:
                break
            
            

""" def main():
    print("Welcome to your password manager! What would you like to do?")
    while True:
        response = input("\nAdd Password: 'Add'\nRemove Password: 'Remove'\nChange Password: 'Change'\nSelection: ")
        response = response.lower()
        if response == 'add' or response == 'remove' or response == 'change':
            break """ # use option shift a to uncomment

main()
    