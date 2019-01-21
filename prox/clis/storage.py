from prox.clis.base import Base
from prox.libs import node_lib
from tabulate import tabulate
from prox.libs import utils
import os


class Storage(Base): 
    """
        usage:
            storage [-N NODE] [-S STORAGE]
            storage content [-N NODE] [-S STORAGE] [-c CONTENT]

        Commands :
            clusters                          list of clusters
            vm                                list of vm

        Options:
        -h --help                             Print usage
        -N node --node=NODE                   Get Node
        -S storage --storage=STORAGE          Get Storage
        -c content --content=CONTENT          Get Content
    """
    def execute(self):
        node = self.args["--node"]
        if not node:
            utils.log_info("Using Default Node : pve")
            node = "pve"
        
        if self.args['content']:
            storage = self.args['--storage']
            if not storage:
                utils.log_err("Set Your Storage")
                exit()
            
            storage = self.args['--storage']
            if not storage:
                utils.log_err("Set Your Storage")
                exit()
            
            content = self.args['--content']
            if not content:
                utils.log_err("Set Your Content")
                exit()
            content_storage = node_lib.get_storage_content(node, storage, content)
            print(content_storage)
            exit()

        storage = self.args['--storage']
        if not storage:
            utils.log_err("Set Your Storage")
            exit()
        detail_storage = node_lib.get_storage_detail(node, storage)
        headers = {
            'storage': "Name Storage", 
            'type': "Type", 
            'total': "Total", 
            'used': "Used",
            'avail': "Available", 
            'shared': "Shared", 
            'active': "Status", 
            'enabled': "Enable", 
            'content': "Content"
        }
        print(tabulate(detail_storage, headers=headers, tablefmt='grid'))

