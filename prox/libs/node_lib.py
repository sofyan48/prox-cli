from prox.libs import login_lib


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
