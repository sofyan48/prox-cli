from prox.clis.base import Base
from prox.libs import clusters_lib
from prox.libs import vm_lib
from tabulate import tabulate
import os


class Ls(Base): 
    """
        usage:
            ls cluster
            ls vm

        Commands :
            clusters                          list of clusters
            vm                                list of vm

        Options:
        -h --help                             Print usage
    """
    def execute(self):
        if self.args['cluster']:
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
            data = vm_lib.list_vm()
            list_vm = list()
            for key in data:
                data_vm = {
                    "vmid": key['vmid'],
                    "name": key['name'],
                    "cpus": key['cpus'],
                    "status": key['status']
                }
                list_vm.append(data_vm)
            headers = {
                "vmid": "ID VM",
                "name": "VM Name",
                "cpus": "vCPUS",
                "status": "Status"
            }
            print(tabulate(list_vm, headers=headers, tablefmt='grid'))
