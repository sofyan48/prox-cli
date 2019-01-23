from prox.clis.base import Base
from getpass import getpass
from prox.libs import login_lib
import os

APP_HOME = login_lib.utils.APP_HOME

class Login(Base): 
    """
        usage:
            login

        Commands :
            login                         Build Yaml File

        Options:
        -h --help                             Print usage
    """
    def execute(self):
        if os.path.exists(APP_HOME+"/.prox.env"):
            print(".prox.env environment file exists. Do You want to remove it?")
            checks = login_lib.utils.question("Choose Y/N ")
            if checks == True:
                username = input("Username: ")
                password = getpass("Password: ")
                auth_url = input("Host: ")
                os.remove(APP_HOME+"/.prox.env")
                login_lib.create_env_file(username, password, auth_url)
        else:
            username = input("Username: ")
            password = getpass("Password: ")
            auth_url = input("Host: ")
            login_lib.create_env_file(username, password, auth_url)

        env = login_lib.utils.get_env_values()
        prox =login_lib.connect_proxmox(env['project_url'], env['username'], env['password'])

        # check login
        if login_lib.utils.read_file("/tmp/prox.pkl"):
            os.remove("/tmp/prox.pkl")
        login_lib.dump_session(prox)
        if not login_lib.check_session():
            login_lib.utils.log_err("Login Not Success")
        login_lib.utils.log_info("Login Success")