from prox.libs import utils
from prox.libs import node_lib
from prox.libs import vm_lib
from prox.libs import clusters_lib
import os

def get_os_template_iso(node, storage):
    content = "iso"
    img_file = "/tmp/.ostemplate.yml"
    content_list = list()

    if utils.read_file(img_file):
        content_list = utils.yaml_parser_file(img_file)["data"]
    else:
        content_storage = node_lib.get_node_storage_content(node, storage)
        for i in content_storage:
            if content == i['content']:
                content_list.append(i['volid'])
        data = {
            "data": content_list
        }
        utils.yaml_create(data, img_file)
    return list(reversed(sorted(content_list)))


def get_os_template_vz(node, storage):
    content = "vztmpl"
    img_file = "/tmp/.osvztmpl.yml"
    content_list = list()
    content_storage = node_lib.get_node_storage_content(node, storage)
    for i in content_storage:
        if content == i['content']:
            content_list.append(i['volid'])
    data = {
        "data": content_list
    }
    utils.yaml_create(data, img_file)
    return list(reversed(sorted(content_list)))

def vm_next(node = None, storage = None):
    vmid_file = "/tmp/.vmid_file.yml"
    vmid_list = list()
    vmid_list_temp = list()
    data = node_lib.vm_next()
    vmid_list_temp.append(data)
    vmid_list = {
        "data": vmid_list_temp
    }
    utils.yaml_create(vmid_list, vmid_file)
    return vmid_list_temp
