from prox.clis.base import Base
from prox.libs import attach_lib
from prox.libs import utils

class Attach(Base): 
    """
        usage:
            attach
            attach vm [-H HOST] [-u USER]


        Commands :
        attach vm                             Atatch / SSH VM

        Options:
        -h --help                             Print usage
        -H host --host=HOST                   Host VM
        -u user --user=USER                   User VM
    """
    def execute(self):
        pass