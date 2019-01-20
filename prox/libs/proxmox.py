from pyproxmox import prox_auth,pyproxmox


def proxmox_auth(host, username, password):
    try:
        prox = prox_auth(host, username, password)
    except Exception:
        raise
    else:
        return pyproxmox(prox)