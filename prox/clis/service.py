from prox.clis.base import Base
from prox.libs import clusters_lib
from tabulate import tabulate
from prox.libs import utils
import os


class Service(Base): 
    """
        usage:
            service [-N NODE]
            service detail [-N NODE] [-s SERVICE]
            service start [-N NODE] [-s SERVICE]
            

        Commands :
            clusters                          list of clusters
            vm                                list of vm

        Options:
        -h --help                             Print usage
        -N node --node=NODE                   Get Node
        -s service --service=SERVICE          Get Node
    """
    def execute(self):
        if self.args['detail']:
            node = self.args["--node"]
            if not node:
                utils.log_warn("Use Default Node : pve")
                node = "pve"
            try:
                service = self.args['--service']
            except Exception:
                service = None
            if not service:
                utils.log_err("Set Service")
                exit()
            list_details = list()
            data = clusters_lib.service_detail(node, service)
            if not data :
                utils.log_err("Data Not Found")
                exit()
            
            list_details.append(data)
            headers = {
                'desc': 'Description', 
                'name': 'Service Name', 
                'state': 'Status',
                'service': 'sshd'
            }
            print(tabulate(list_details, headers=headers, tablefmt='grid'))
            exit()
            
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
                    "name": i['name']
                }
                list_service.append(data_service)
            headers = {
                "name": "Service Name"
            }
            print(tabulate(list_service, headers=headers, tablefmt='grid'))
            exit()
        utils.log_warn("Using Default Node : pve")
        data = clusters_lib.cluster_service("pve")
        if not data:
            utils.log_err("Data Not Found")
            exit()
        list_service = list()
        for i in data:
            data_service = {
                "name": i['name']
            }
            list_service.append(data_service)
        headers = {
            "name": "Service Name"
        }
        print(tabulate(list_service, headers=headers,tablefmt='grid'))
        exit()
