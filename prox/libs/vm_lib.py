from prox.libs import login_lib


def get_auth():
    try:
        prox = login_lib.load_dumped_session()
    except Exception as e:
        print(e)
        exit()
    else:
        return prox

def list_vm():
    prox = get_auth()
    vm_list = prox.getVm()['data']
    return vm_list

