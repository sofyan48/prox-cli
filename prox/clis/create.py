from prox.clis.base import Base
from getpass import getpass
from prox.libs import login_lib
from prox.libs import node_lib
from prox.libs import vm_lib
from prox.libs import network_lib
from prox.libs import utils
from prox.libs import ncurses, prompt
import os

class Create(Base): 
    """
        usage:
            create [-i] [-f PATH]
            create [-t TEMPLATE] [-i]
            create vm
            create pool

        Commands :
            create                          Build Yaml File

        Options:
        -h --help                           Print usage
        -f PATH --file=PATH                 Set neo manifest file
        -t TEMPLATE --template TEMPLATE     Create neo.yml, TEMPLATE is ENUM(clusters,instances,networks)
        -i --interactive                    Interactive form with ncurses mode
    """
    def execute(self):
        if self.args["--template"]:
            if self.args["--template"] in ('pool', 'instances',
                                           'network', "storage"):
                tmpl = self.args["--template"]

                if self.args["--interactive"]:
                    ncurses.init(stack=tmpl)
                else:
                    prompt.init(stack=tmpl)
            exit()

        if self.args["vm"]:
            if self.args["--interactive"]:
                print(ncurses.init(stack="instances", project="vm"))
            else:
                print(prompt.init(stack="instances", project="vm"))

        set_file = self.args["--file"]
        default_file = utils.check_manifest_file()

        if set_file:
            if os.path.exists(set_file):
                default_file = set_file
            else:
                utils.log_err("{} file is not exists!".format(set_file))
                exit()

        if not default_file:
            utils.log_err("Can't find prox.yml manifest file!")
            q_stack = utils.question(
                "Do you want to generate pro.yml manifest? ")

            if q_stack:
                if self.args["--interactive"]:
                    print(ncurses.init())
                else:
                    print(prompt.init())
                q_deploy = utils.question("Continue to deploy? ")
                if q_deploy:
                    default_file = "prox.yml"
                else:
                    exit()
            else:
                exit()
        else:
            q_deploy = utils.question("Continue to deploy? ")
            if q_deploy:
                default_file = "prox.yml"
            else:
                exit()
