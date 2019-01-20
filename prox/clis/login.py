from prox.clis.base import Base
from prox.libs import login
from getpass import getpass
import os


CURR_DIR = os.getcwd()

class Login(Base):
    """
        usage:
            login
            login neo
            login docker

        Build Project

        Options:
        -h --help                             Print usage
    """

    def execute(self):
        if self.args['neo']:
            username = input("Username: ")
            password = getpass("Password: ")
            login.login(username , password)

