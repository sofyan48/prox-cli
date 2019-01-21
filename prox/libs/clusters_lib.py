from prox.libs import login_lib


def get_auth():
    try:
        prox = login_lib.load_dumped_session()
    except Exception as e:
        print(e)
        exit()
    else:
        return prox

def list_cluster():
    prox = get_auth()
    cl_list = prox.getClusterStatus()
    return cl_list




