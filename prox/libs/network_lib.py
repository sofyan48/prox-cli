from prox.libs import login_lib

def get_auth():
    try:
        prox = login_lib.load_dumped_session()
    except Exception as e:
        print(e)
        exit()
    else:
        return prox

def get_network(node):
    prox = get_auth()
    network = prox.getNodeNetworks(node)
    return network['data']