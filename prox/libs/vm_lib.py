from prox.libs import login_lib
from prox.libs import utils

def get_auth(session=None):
    if not session:
        try:
            prox = login_lib.load_dumped_session()
        except Exception as e:
            print(e)
            exit()
        else:
            return prox

def get_vm_detail(node, vm_id, session=None):
    prox = get_auth(session)
    vm_detail = prox.getVirtualIndex(node, vm_id)
    return vm_detail['data']

def get_vm_status(node, vm_id, session=None):
    prox = get_auth(session)
    vm_status = prox.getVirtualStatus(node, vm_id)
    return vm_status['data']

def get_vm_action(node, vm_id, action, session=None):
    prox = get_auth(session)
    vm_status = prox.getVirtualInfo(node, vm_id, action)
    return vm_status['data']

def get_vm_rrd(node, vm_id, session=None):
    prox = get_auth(session)
    vm_rrd = prox.getVirtualRRD(node, vm_id)
    return vm_rrd['data']

def delete_vm(node, vm_id, session=None):
    prox = get_auth(session)
    vm_delete = prox.deleteVirtualMachine(node, vm_id)
    return vm_delete

def reset_vm(node, vm_id, session=None):
    prox = get_auth(session)
    vm = prox.resetVirtualMachine(node, vm_id)
    if vm['data']:
        return vm['data']
    else:
        return vm['error']

def resume_vm(node, vm_id, session=None):
    prox = get_auth(session)
    vm = prox.resumeVirtualMachine(node, vm_id)
    if vm['data']:
        return vm['data']
    else:
        return vm['error']

def start_vm(node, vm_id, session=None):
    prox = get_auth(session)
    vm = prox.startVirtualMachine(node, vm_id)
    if vm['data']:
        return vm['data']
    else:
        return vm['error']

def shutdown_vm(node, vm_id, session=None):
    prox = get_auth(session)
    vm = prox.shutdownVirtualMachine(node, vm_id)
    if vm['data']:
        return vm['data']
    else:
        return vm['error']

def stop_vm(node, vm_id, session=None):
    prox = get_auth(session)
    vm = prox.stopVirtualMachine(node, vm_id)
    if vm['data']:
        return vm['data']
    else:
        return vm['error']

def suspesn_vm(node, vm_id, session=None):
    prox = get_auth(session)
    vm = prox.suspendVirtualMachine(node, vm_id)
    if vm['data']:
        return vm['data']
    else:
        return vm['error']


def vnc_vm(node, vm_id, session=None):
    prox = get_auth(session)
    vm = prox.vncproxyVirtualMachine(node, vm_id)
    if vm['data']:
        return vm['data']
    else:
        return vm['error']