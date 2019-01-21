from prox.clis.base import Base
from prox.libs import network_lib
from tabulate import tabulate
from prox.libs import utils
import os


class Interface(Base): 
    """
        usage:
            interface [-N NODE] [-I INTERFACE]

        Commands :
            clusters                          list of clusters
            vm                                list of vm

        Options:
        -h --help                             Print usage
        -N node --node=NODE                   Get Node
        -I interface --interface=INTERFACE    Get Interface Details
    """
    def execute(self):
        node = self.args["--node"]
        if not node:
            utils.log_info("Using Default Node : pve")
            node = "pve"

        interface = self.args['--interface']
        if not interface:
            utils.log_err("Set Your Interface")
            exit()
        
        data = network_lib.get_interface_details(node, interface)
        detail_interface = list()
        if not data:
            utils.log_err("Data Not Found")
            exit()
        detail_interface.append(data)
        headers = {
            'exists': "Exists", 
            'type': 'Type', 
            'method': 'Method', 
            'method6': 'Method6', 
            'priority': "Priority", 
            'families': "Families"
        }
        print(tabulate(detail_interface, headers=headers, tablefmt='grid'))