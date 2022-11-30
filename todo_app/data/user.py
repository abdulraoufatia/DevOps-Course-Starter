from flask_login import UserMixin
import os

class User(UserMixin):
    def __init__(self, id):
        self.id = id

    def writer_role(self): 
        return self.id == os.getenv("id")