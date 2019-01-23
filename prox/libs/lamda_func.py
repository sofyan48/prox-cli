from prox.libs import utils
from prox.libs import node_lib
from prox.libs import vm_lib
from prox.libs import clusters_lib


def get_os_template(node, storage, content):
    content_storage = node_lib.get_node_storage_content(node, storage)
    content_list = list()
    for i in content_storage:
        if content == i['content']:
            content_list.append(i)
    return content_list