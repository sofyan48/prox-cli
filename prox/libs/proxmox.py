from pyproxmox import *


def proxmox_auth(host, username, password):
    try:
        prox = prox_auth(host, username, password)
    except Exception:
        raise
    else:
        return prox

def list_vm(prox):
    try:
        list_vm = prox.getClusterStatus()
    except Exception :
        raise

    return list_vm