from prox.libs.proxmox.pyproxmox import prox_auth, pyproxmox
import urllib3

urllib3.disable_warnings()

def proxmox_auth(host, username, password):
    try:
        prox = prox_auth(host, username, password)
    except Exception:
        raise
    else:
        return pyproxmox(prox)