# from passlib.hash import pbkdf2_sha256
from prox.libs import utils
from prox.libs import proxmox_lib
import os
import dill

APP_HOME = utils.APP_HOME

def create_env_file(username, password, auth_url = None, port = None):
    try:
        env_file = open("{}/.prox.env".format(APP_HOME), "w+")
        env_file.write("OS_USERNAME=%s\n" % username)
        env_file.write("OS_PASSWORD=%s\n" % password)
        env_file.write("OS_PROJECT_URL=%s\n" % auth_url)
        env_file.write("OS_PROJECT_PORT=%s\n" % port)
        env_file.close()
        return True
    except Exception as e:
        print(e)
        return False


def dump_session(sess):
    try:
        with open('/tmp/prox.pkl', 'wb') as f:
            dill.dump(sess, f)
    except Exception:
        utils.log_err("Dump session failed")


def load_dumped_session():
    try:
        if check_session():
            sess = None
            with open('/tmp/prox.pkl', 'rb') as f:
                sess = dill.load(f)
            return sess
        else:
            return load_dumped_session()
    except Exception as e:
        utils.log_err("Loading Session Failed")
        utils.log_err("Please login first")
        utils.log_err(e)


def check_session():
    return os.path.isfile("/tmp/prox.pkl")


def logout():
    if os.path.exists(APP_HOME+"/.prox.env"):
        os.remove(APP_HOME+"/.prox.env")
        os.remove("/tmp/prox.pkl")
    else:
        print("Not Current Sessions")

def connect_proxmox(host, username, password):
    prox_at = proxmox_lib.proxmox_auth(host, username, password)
    return prox_at




