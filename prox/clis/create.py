from prox.clis.base import Base
from getpass import getpass
from prox.libs import utils, create_libs
from prox.libs import ncurses, prompt
import os

class Create(Base): 
    """
        usage:
            create [-N NODE] [-i] [-f PATH]
            create [-t TEMPLATE] [-i]
            create vm
            create pool

        Commands :
            create                          Build Yaml File

        Options:
        -h --help                           Print usage
        -f PATH --file=PATH                 Set prox manifest file
        -t TEMPLATE --template TEMPLATE     Create prox.yml, TEMPLATE is ENUM(pool,instances,networks)
        -i --interactive                    Interactive form with ncurses mode
        -N node --node=NODE                   Get Node
    """
    def execute(self):
        node = self.args["--node"]
        if not node:
            utils.log_info("Using Default Node : pve")
            node = "pve"

        if self.args["--template"]:
            if self.args["--template"] in ('pool', 'instances',
                                           'network', "storage"):
                tmpl = self.args["--template"]

                if self.args["--interactive"]:
                    ncurses.init(node, stack=tmpl)
                else:
                    prompt.init(node, stack=tmpl)
            exit()

        if self.args["vm"]:
            if self.args["--interactive"]:
                print(ncurses.init(node, stack="instances", project="vm"))
            else:
                print(prompt.init(node, stack="instances", project="vm"))

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
                    print(ncurses.init(node))
                else:
                    print(prompt.init(node))
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

        deploy_init = create_libs.initialize(node,default_file)

        try:
            create_libs.do_create(deploy_init)
        except Exception as e:
            raise
            # utils.log_err(e)
            # utils.log_err("Deploying Stack failed...")
            exit()
