from prox.libs import login_lib

def get_auth():
    try:
        prox = login_lib.load_dumped_session()
    except Exception as e:
        print(e)
        exit()
    else:
        return prox

def get_interface(node):
    prox = get_auth()
    network = prox.getNodeNetworks(node)
    return network['data']

def get_interface_details(node, interface):
    prox = get_auth()
    network = prox.getNodeInterface(node, interface)
    return network['data']

def delete_node_network(node):
    prox = get_auth()
    list_network = prox.deleteNodeNetworkConfig(node)
    return list_network['data']

def delete_node_interface(node):
    prox = get_auth()
    list_network = prox.deleteNodeInterface(node)
    return list_network['data']
    