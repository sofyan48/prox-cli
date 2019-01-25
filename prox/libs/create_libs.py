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
    else:
        return session

def create_vm(node, post_data, session=None):
    prox = get_auth(session)
    try:
        data_create = prox.createVirtualMachine(node, post_data)
    except Exception as e:
        print(e)
    else:
        return data_create

def create_containers(node, post_data, session=None):
    prox = get_auth(session)
    try:
        data_create = prox.createOpenvzContainer(node, post_data)
    except Exception as e:
        print(e)
    else:
        return data_create


def initialize(node, manifest_fie):
    if not node:
        node = "pve"
    init = list()
    utils.log_info("Initialization....")
    key = utils.do_deploy_dir(manifest_fie)

    for stack in utils.initdir(key): 
        for project in key["stack"][stack]:
            try:
                parameters = key["data"][stack][project]["parameters"]
            except:
                parameters = None

            dest = "{}/{}/{}".format(key["deploy_dir"], stack, project)
            utils.log_info("Build {} {} template".format(project, stack))
            utils.log_info("Done...")
            """ Stack init dict """
            stack_init = {}
            stack_init["dir"] = dest
            stack_init["project"] = project
            stack_init["stack"] = stack
            stack_init["node"] = node
            stack_init["template"] = key["data"][stack][project]['template']
            stack_init["env_file"] = False

            if not utils.check_folder(dest):
                utils.create_folder(dest)

            if parameters:
                utils.log_info("Create {} {} environment file".format(
                    project, stack))
                data_path= {
                    "parameters": parameters
                }
                utils.yaml_create(data_path,"{}/env.yml".format(dest))
                utils.log_info("Done...")
                stack_init["env_file"] = "{}/env.yml".format(dest)

            init.append(stack_init)

    """ Reformat squences deploy """
    if utils.check_key(key["data"], "deploy"):
        if len(key["data"]["deploy"]) > 0:
            set_sequence = list()
            for deploy in key["data"]["deploy"]:
                set_deploy = deploy.split(".")
                set_stack = set_deploy[0]
                set_project = set_deploy[1]
                set_sequence.append([
                    new_init for new_init in init
                    if (new_init["stack"] == set_stack) and (
                        new_init["project"] == set_project)
                ][0])
            init = set_sequence
    utils.yaml_create(init ,"{}/deploy.yml".format(key["deploy_dir"]))
    return init


def do_create(initialize):
    # dir_deploy = None
    # project_name = None
    # stack_name = None
    env_parameters = list()
    data_env = list()
    node = None
    data_params = list()
    template = None

    for deploy in initialize:
        # dir_deploy = deploy['dir']
        # project_name = deploy['project']
        # stack_name = deploy['stack']
        env_parameters = deploy['env_file']
        data_env = utils.yaml_parser_file(env_parameters)
        node = deploy['node']
        data_params = data_env['parameters']
        template = deploy['template']

    if template == 'containers':
        data_create = create_containers(node, data_params)
    elif template == 'vm':
        data_create = create_vm(node, data_params)
    else:
        utils.log_err("COMING SOON")
    return data_create


