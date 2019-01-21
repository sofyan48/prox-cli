from prox.libs import login_lib
from prox.libs import utils

def get_auth():
    try:
        prox = login_lib.load_dumped_session()
    except Exception as e:
        print(e)
        exit()
    else:
        return prox

def list_vm_by_node(node):
    prox = get_auth()
    vm_list = prox.getNodeVirtualIndex(node)
    return vm_list['data']

def list_container_by_node(node):
    prox = get_auth()
    vm_list = prox.getNodeContainerIndex(node)
    return vm_list['data']

def vm_next():
    prox = get_auth()
    vm_next = prox.getClusterVmNextId()
    return vm_next['data']

def get_storage(node):
    prox = get_auth()
    list_storage = prox.getNodeStorage(node)
    return list_storage['data']

def get_storage_detail(node, storage):
    prox = get_auth()
    try:
        data = prox.getNodeStorage(node)
    except Exception as e:
        print(e)
        raise e
    detail_storage = list()
    for i in data['data']:
        if i['storage'] == storage:
            content = None
            content = i['content']
            content = content.split(",")
            detail_storage.append({
                "storage": i['storage'],
                "avail": i['avail'],
                "type": i['type'],
                "total": i['total'],
                "used": i['used'],
                "shared": i['shared'],
                "active": i['active'],
                "enabled": i['enabled'],
                "content": content,
            })
            return detail_storage

def get_storage_content(node, storage, volume):
    prox = get_auth()
    list_storage = prox.getStorageVolumeData(node, storage, volume)
    return list_storage['data']