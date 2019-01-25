from prox.libs import login_lib


def get_auth(session=None):
    if not session:
        try:
            prox = login_lib.load_dumped_session()
        except Exception as e:
            print(e)
            exit()
        else:
            return prox
    else:
        return session

def get_interface(node, session=None):
    prox = get_auth(session)
    network = prox.getNodeNetworks(node)
    return network['data']

def get_interface_details(node, interface, session=None):
    prox = get_auth(session)
    network = prox.getNodeInterface(node, interface)
    return network['data']

def delete_node_network(node, session=None):
    prox = get_auth(session)
    list_network = prox.deleteNodeNetworkConfig(node)
    return list_network['data']

def delete_node_interface(node, session=None):
    prox = get_auth(session)
    list_network = prox.deleteNodeInterface(node)
    return list_network['data']
    