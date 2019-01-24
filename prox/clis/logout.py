from prox.clis.base import Base
from prox.libs import login_lib
import os

APP_HOME = login_lib.utils.APP_HOME

class Logout(Base): 
    """
        usage:
            login

        Commands :
            login                         Build Yaml File

        Options:
        -h --help                             Print usage
    """
    def execute(self):
        login_lib.logout()