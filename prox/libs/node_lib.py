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

def get_finish_task(node):
    prox = get_auth()
    list_finish = prox.getNodeFinishedTasks(node)
    return list_finish

def get_node_dns(node):
    prox = get_auth()
    list_dns = prox.getNodeDNS(node)
    return list_dns['data']

def get_node_status(node):
    prox = get_auth()
    list_status = prox.getNodeStatus(node)
    return list_status['data']

def get_node_syslog(node):
    prox = get_auth()
    list_syslog= prox.getNodeSyslog(node)
    return list_syslog['data']

def get_node_rrd(node, path=None):
    prox = get_auth()
    png_rrd= prox.getNodeRRD(node)
    return png_rrd

def get_node_rrd_data(node, path=None):
    prox = get_auth()
    rrd_data= prox.getNodeRRDData(node)
    return rrd_data

def get_node_beans(node):
    prox = get_auth()
    beans_data= prox.getNodeBeans(node)
    return beans_data['data']

def get_storage_volume(node, storage, volume):
    prox = get_auth()
    list_storage = prox.getStorageVolumeData(node, storage, volume)
    return list_storage['data']

def get_node_storage_content(node,storage):
    prox = get_auth()
    list_storage = prox.getNodeStorageContent(node, storage)
    return list_storage['data']

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

def get_os_template(node, storage, content):
    content_storage = get_node_storage_content(node, storage)
    content_list = list()
    for i in content_storage:
        if content == i['content']:
            content_list.append(i)
    return content_list


