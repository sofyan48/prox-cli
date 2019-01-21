from prox.clis.base import Base
from prox.libs import clusters_lib
from prox.libs import vm_lib
from prox.libs import network_lib
from prox.libs import utils
from tabulate import tabulate
import os


class Ls(Base): 
    """
        usage:
            ls cluster [-i | --interface] [-N NODE]
            ls vm [-n | --next]
            

        Commands :
            clusters                          list of clusters
            vm                                list of vm

        Options:
        -h --help                             Print usage
        -i --interface                        cluster interface
        -n --next                             vm next
        -N node --node=NODE                   Get Node  
    """
    def execute(self):
        if self.args['cluster']:
            if self.args['--interface']:
                node = self.args['--node']
                data = network_lib.get_network(node)
                list_interface = list()
                for i in data:
                    data_interface = {
                        "interface": i['iface'],
                        "type": i['type'],
                        "families": i['families']
                    }
                    list_interface.append(data_interface)

                headers = {
                    "interface": "Interface",
                    "type": "Type",
                    "families": "Families"
                }
                print(tabulate(list_interface, headers=headers, tablefmt='grid'))
                exit()
            headers = {
                'nodeid': "NODE" , 
                'ip' : "IP", 
                'name' : "Name", 
                "type" : "Type", 
                "id" : "ID", 
                "online" : "Online",
                "level": "Level",
                "local": "Local"
            }
            list_cluster = clusters_lib.list_cluster()["data"]
            print(tabulate(list_cluster, headers=headers,tablefmt='grid'))
            exit()
        if self.args['vm']:
            if self.args['--next']:
                cl_next = vm_lib.cluster_next()
                utils.log_info(cl_next)
                exit()
            
            data = vm_lib.list_vm()
            list_vm = list()
            for key in data:
                data_vm = {
                    "vmid": key['vmid'],
                    "name": key['name'],
                    "cpus": key['cpus'],
                    "memory": key['mem'],
                    "status": key['status']
                }
                list_vm.append(data_vm)
            headers = {
                "vmid": "ID VM",
                "name": "VM Name",
                "cpus": "vCPUS",
                "memory": "RAM",
                "status": "Status"
            }
            print(tabulate(list_vm, headers=headers, tablefmt='grid'))
            exit()
