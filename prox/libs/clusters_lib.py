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

def list_cluster():
    prox = get_auth()
    cl_list = prox.getClusterStatus()
    return cl_list

def cluster_service(node, session=None):
    prox = get_auth(session)
    cluster_service = prox.getNodeServiceList(node)
    return cluster_service['data']

def service_detail(node, service, session=None):
    prox = get_auth(session)
    detail_service = prox.getNodeServiceState(node, service)
    return detail_service['data']


