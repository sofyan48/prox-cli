from prox.clis.base import Base
from prox.libs import vm_lib
from tabulate import tabulate
from prox.libs import utils
import os


class VM(Base): 
    """
        usage:
            vm [-N NODE] [-i VMID] [-a ACTION]
            vm info [-N NODE] [-i VMID] [-a ACTION]
            vm rrd [-N NODE] [-i VMID]


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
        
        if self.args['info']:
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
                            utils.log_info(i+" "+str(data[i]))
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

        if self.args['rrd']:
            # not complete no representing data in process
            data = vm_lib.get_vm_rrd(node, vm_id)
            utils.log_info("Coming soon")
            exit()

        action = self.args['--action']
        if not action: 
            data_vm = vm_lib.get_vm_detail(node, vm_id)
            headers = {
                "subdir": "Action"
            }
            print(tabulate(data_vm, headers=headers, tablefmt="grid"))
            exit()
        
        if action:
            # Not Fix in View Error detecting tabulate
            data_vm = vm_lib.get_vm_detail(node, vm_id)
            # list_data_vm = list()
            for i in data_vm:
                if action == i['subdir']:
                    data_action = vm_lib.get_vm_action(node, vm_id, i['subdir'])
                    if type(data_action) == dict:
                        for key in data_action:
                            # data = {
                            #     key : data_action[key]
                            # }
                            # 
                            # list_data_vm.append(data)
                            utils.log_info(str(key)+" | "+str(data_action[key]))
                        break
                    else:
                        utils.log_info(i+" "+str(i['subdir']))
                        exit
            # print(tabulate(data_vm_fix, headers="keys", tablefmt="grid"))
            exit()

        




        