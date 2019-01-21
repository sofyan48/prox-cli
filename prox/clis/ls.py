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
            ls cluster [-i | --iface] [-N NODE] [-s | --service]
            ls vm [-n | --next] [-N NODE]
            ls container [-N NODE]
            ls interface [-N NODE] [-I INTERFACE]
            
            

        Commands :
            clusters                          list of clusters
            vm                                list of vm

        Options:
        -h --help                             Print usage
        -i --iface                            cluster interface
        -s --service                          cluster service
        -n --next                             vm next
        -N node --node=NODE                   Get Node  default by 'pve'
        -I node --interface=INTERFACE         Get Interface Details
    """
    def execute(self):
        if self.args['cluster']:
            if self.args['--service']:
                try:
                    node = self.args["--node"]
                except Exception:
                    node = None
                if node:
                    data = clusters_lib.cluster_service(node)
                    if not data:
                        utils.log_err("Data Not Found")
                        exit()
                    list_service = list()
                    for i in data:
                        data_service = {
                            "name": i['name'],
                            "state": i['state'],
                            "desc": i['desc']
                        }
                        list_service.append(data_service)
                    headers = {
                        "name": "Service Name",
                        "state": "Service State",
                        "desc": "Description"
                    }
                    print(tabulate(list_service, headers=headers,tablefmt='grid'))
                    exit()
                data = clusters_lib.cluster_service("pve")
                if not data:
                    utils.log_err("Data Not Found")
                    exit()
                list_service = list()
                for i in data:
                    data_service = {
                        "name": i['name'],
                        "state": i['state'],
                        "desc": i['desc']
                    }
                    list_service.append(data_service)
                headers = {
                    "name": "Service Name",
                    "state": "Service State",
                    "desc": "Description"
                }
                print(tabulate(list_service, headers=headers,tablefmt='grid'))
                exit()
            
            if self.args['--iface']:
                try:
                    node = self.args['--node']
                except Exception:
                    node = None
                if not node:
                    utils.log_err("Set Your Node")
                    exit()
                data = network_lib.get_interface(node)
                if not data:
                    utils.log_err("Data Not Found")
                    exit()
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

        if self.args['interface']:
            def_node = "pve"
            try:
                node = self.args["--node"]
            except Exception:
                utils.log_info("Using Default Node : pve")
                node = def_node
            
            try:
                interface = self.args['interface']
            except Exception:
                interface = None

            if not interface:
                utils.log_err("Set Your Interface")
                exit()
            
            data = network_lib.get_interface_details(node, interface)
            if not data:
                utils.log_err("Data Not Found")
                exit()
            print("WIP: Not Data In Testing")
            

        
            