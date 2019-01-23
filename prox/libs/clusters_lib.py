from prox.libs import login_lib


def get_auth(session = None):
    if not session:
        prox = login_lib.load_dumped_session()
    else:
        return session
    return prox

def list_cluster():
    prox = get_auth()
    a = prox.getClusterStatus()
    print(a)

