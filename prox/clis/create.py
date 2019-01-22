from prox.clis.base import Base
from getpass import getpass
from prox.libs import login_lib
from prox.libs import node_lib
from prox.libs import vm_lib
from prox.libs import network_lib
from prox.libs import utils
import os

class Create(Base): 
    """
        usage:
            create

        Commands :
            create                         Build Yaml File

        Options:
        -h --help                          Print usage
    """
    def execute(self):
        print("CREATE")