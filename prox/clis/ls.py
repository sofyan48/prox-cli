from prox.clis.base import Base
from prox.libs import clusters_lib
import os


class Ls(Base): 
    """
        usage:
            ls cluster

        Commands :
            clusters                          list of clusters

        Options:
        -h --help                             Print usage
    """
    def execute(self):
        if self.args['cluster']:
            clusters_lib.list_cluster()
            exit()
