from prox.clis.base import Base
from prox.libs import clusters_lib
from prox.libs import node_lib
from prox.libs import network_lib
from prox.libs import utils
from tabulate import tabulate
import os


class Ls(Base): 
    """
        usage:
            ls cluster [-N NODE]
            ls vm [-n | --next] [-N NODE]
            ls container [-N NODE]
            ls storage [-N NODE]
            ls network [-N NODE]

        Commands :
            clusters                          list of clusters
            vm                                list of vm

        Options:
        -h --help                             Print usage
        -n --next                             vm next
        -N node --node=NODE                   Get Node  default by 'pve'
    """
    def execute(self):
        if self.args['network']:
            node = self.args['--node']
            if not node:
                node="pve"
                utils.log_warn("Using Default Node | -N node to set node")
            data = network_lib.get_interface(node)
            if not data:
                utils.log_err("Data Not Found")
                exit()
            list_interface = list()
            print(data)
            for i in data:
                data_interface = {
                    "interface": i['iface'],
                    "type": i['type'],
                }
                list_interface.append(data_interface)

            headers = {
                "interface": "Interface",
                "type": "Type",
            }
            print(tabulate(list_interface, headers=headers, tablefmt='grid'))
            exit()
            
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
            if self.args['--next']:
                cl_next = node_lib.vm_next()
                utils.log_info(cl_next)
                exit()
            
            try:
                node = self.args["--node"]
            except Exception:
                node = None
            if node:
                data = node_lib.list_vm_by_node(node)
                if not data:
                    utils.log_err("Data Not Found")
                    exit()
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
            
            utils.log_warn("Using default node : pve ")
            data = node_lib.list_vm_by_node("pve")
            if not data:
                utils.log_err("Data Not Found")
                exit()
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

        if self.args['container']:
            try:
                node = self.args["--node"]
            except Exception:
                node = None
            if node:
                data = node_lib.list_container_by_node("pve")
                if not data:
                    utils.log_err("Data Not Found")
                    exit()
                print("WIP: Not Data In Testing")
                exit()
            data = node_lib.list_container_by_node("pve")
            if not data:
                utils.log_err("Data Not Found")
                exit()
            print("WIP: Not Data In Testing")

        if self.args['storage']:
            node = self.args['--node']
            if not node:
                utils.log_warn("Using Default Node : pve")
                node = "pve"
            data = node_lib.get_storage(node)
            if not data:
                utils.log_err("Data Not Found")
                exit()
            list_storage = list()
            for i in data:
                storage={
                    "storage": i['storage'],
                    "total": i["total"],
                    "used": i["used"],
                    "avail": i['avail']
                }
                list_storage.append(storage)
            headers = {
                "storage": "Name Storage",
                "total": "Total",
                "used": "Used",
                "avail": "Available"
            }
            print(tabulate(list_storage, headers=headers, tablefmt='grid'))
            exit()
            

        
            