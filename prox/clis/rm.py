from prox.clis.base import Base
from prox.libs import node_lib, network_lib, vm_lib
from prox.libs import utils

class Rm(Base): 
    """
        usage:
            rm [-N NODE]
            rm vm [-N NODE] [-i VMID]
            rm network [-N NODE] [-I INTERFACE]


        Commands :
        rm vm                                Remove VM
        rm network

        Options:
        -h --help                             Print usage
        -N node --node=NODE                   Get Node
        -i vmid --vmid=VMID                   Get vm
        -I interface --interface=INTERFACE    Set Network interface to delete
    """
    def execute(self):
        node = self.args["--node"]
        if not node:
            utils.log_info("Using Default Node : pve")
            node = "pve"

        if self.args['vm']:
            vmid = self.args['--vmid']
            if vmid:
                # WITH ARGUMEN VM ID
                print("RM WITH ARGUMEN"+ vmid)
                # code here
                exit()

            # No Argumen VM ID
            print("RM VM")
            # Code Here
            # check prox.yml to data vmid
            exit()
        
        # rm command
        # code here
        # check yaml to data action