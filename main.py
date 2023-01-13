import os


users = []

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