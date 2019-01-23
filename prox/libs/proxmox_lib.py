<<<<<<< HEAD:prox/libs/proxmox.py
from pyproxmox import prox_auth,pyproxmox
=======
from prox.libs.proxmox.pyproxmox import prox_auth, pyproxmox
>>>>>>> 70b4c6f144712d62a2ebce15a922fd3645a09794:prox/libs/proxmox_lib.py
import urllib3

urllib3.disable_warnings()

def proxmox_auth(host, username, password):
    try:
        prox = prox_auth(host, username, password)
    except Exception:
        raise
    else:
        return pyproxmox(prox)