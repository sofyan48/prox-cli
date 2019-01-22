from prox.clis.base import Base
from prox.libs import vm_lib
from tabulate import tabulate
from prox.libs import utils
import os


class VM(Base): 
    """
        usage:
            vm [-N NODE] [-i VMID]
            vm status [-N NODE] [-i VMID] [-a ACTION]

        Commands :
            vm                                list of vm

        Options:
        -h --help                             Print usage
        -N node --node=NODE                   Get Node
        -i vmid --vmid=VMID                   Get vm
        -a action --action=ACTION             Get ACTION
    """
    def execute(self):
        node = self.args["--node"]
        if not node:
            utils.log_info("Using Default Node : pve")
            node = "pve"

        vm_id = self.args["--vmid"]
        if not vm_id:
            utils.log_err("Set VM_ID : -i VM_ID")
            exit()
        
        if self.args['status']:
            data = vm_lib.get_vm_status(node, vm_id)
            action = self.args['--action']
            if action:
                details_status = list()
                for i in data:
                    if i == action:
                        if type(data[i]) == dict:
                            details_status.append(data[i])
                            break
                        else:
                            utils.log_info(i+" "+data[i])
                            exit()
                print(tabulate(details_status, headers="keys", tablefmt="grid"))
                exit()

            list_data = list()
            for i in data:
                if type(data[i]) != dict:
                    list_data.append({
                        "action": i
                    })
                else: 
                    list_data.append({
                        "action":i
                    })
            print(tabulate(list_data, headers="keys", tablefmt="grid"))
            exit()

        
        data_vm = vm_lib.get_vm_detail(node, vm_id)
        headers = {
            "subdir": "Action"
        }
        print(tabulate(data_vm, headers=headers, tablefmt="grid"))
        exit()




        