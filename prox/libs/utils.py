import yaml
import os
import shutil
import git
import requests
import zipfile 
from dotenv import load_dotenv
import coloredlogs
import logging
import npyscreen

from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter

APP_HOME = os.path.expanduser("~")
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def form_generator(form_title, fields):
    def myFunction(*args):
        form = npyscreen.Form(name=form_title)
        result = {}
        for field in fields:
            t = field["type"]
            k = field["key"]
            del field["type"]
            del field["key"]

            result[k] = form.add(getattr(npyscreen, t), **field)
        form.edit()
        return result

    return npyscreen.wrapper_basic(myFunction)


def prompt_generator(form_title, fields):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print(form_title)

    data = {}
    for field in fields:
        if field['type'] == 'TitleSelectOne':
            print('{} : '.format(field['name']))
            completer = WordCompleter(field['values'], ignore_case=True)
            for v in field['values']:
                print('- {}'.format(v))
            text = None

            while text not in field['values']:
                text = prompt('Enter your choice : ', completer=completer)

            data[field['key']] = text
        elif field['type'] == 'TitleSelect':
            print('{} : '.format(field['name']))
            completer = WordCompleter(field['values'], ignore_case=True)
            for v in field['values']:
                print('- {}'.format(v))
            data[field['key']] = prompt(
                'Enter your choice or create new : ', completer=completer)
        elif field['type'] == 'TitlePassword':
            data[field['key']] = prompt(
                '{} : '.format(field['name']), is_password=True)
        else:
            data[field['key']] = prompt('{} : '.format(field['name']))
        print('------------------------------')
    return data


def isint(number):
    try:
        to_float = float(number)
        to_int = int(to_float)
    except ValueError:
        return False
    else:
        return to_float == to_int

def isfloat(number):
    try:
        float(number)
    except ValueError:
        return False
    else:
        return True

def repodata():
    abs_path = os.path.dirname(os.path.realpath(__file__))
    repo_file = "{}/templates/repo.yml".format(abs_path)
    return yaml_parser_file(repo_file)


def get_index(dictionary):
    return [key for (key, value) in dictionary.items()]


def check_key(dict, val):
    try:
        if dict[val]:
            return True
    except Exception:
        return False

def question(word): 
    answer = False
    while answer not in ["y", "n"]:
        answer = input("{} [y/n]? ".format(word)).lower().strip()

    if answer == "y":
        answer = True
    else:
        answer = False
    return answer

def log_info(stdin):
    coloredlogs.install()
    logging.info(stdin)


def log_warn(stdin):
    coloredlogs.install()
    logging.warn(stdin)


def log_err(stdin):
    coloredlogs.install()
    logging.error(stdin)

def check_keys(obj, keys):
    chek = None
    try:
        chek = obj[keys]
    except Exception:
        return False
    else:
        return True


def template_git(url, dir):
    try:
        chk_repo = os.path.isdir(dir)
        if chk_repo:
            shutil.rmtree(dir)
        git.Repo.clone_from(url, dir)
        return True
    except Exception as e:
        print(e)
        return False

def yaml_parser_file(file):
    with open(file, 'r') as stream:
        try:
            data = yaml.load(stream)
            return data
        except yaml.YAMLError as exc:
            print(exc)

def yaml_parser(stream):
    try:
        data = yaml.load(stream)
        print(data)
        return data
    except yaml.YAMLError as exc:
        print(exc)


def yaml_create(stream, path):
    with open(path, 'w') as outfile:
        try:
            yaml.dump(stream, outfile, default_flow_style=False)
        except yaml.YAMLError as exc:
            print(exc)
        else:
            return True

def check_manifest_file():
    prox_file = None
    cwd = os.getcwd()
    if os.path.exists("{}/prox.yaml".format(cwd)):
        prox_file = "{}/prox.yaml".format(cwd)
    if os.path.exists("{}/prox.yml".format(cwd)):
        prox_file = "{}/prox.yml".format(cwd)
    return prox_file


def yaml_writeln(stream, path):
    with open(path, '+a') as outfile:
        try:
            yaml.dump(stream, outfile, default_flow_style=False)
        except yaml.YAMLError as exc:
            print(exc)
        else:
            return True


def yaml_read(path):
    with open(path, 'r') as outfile:
        try:
            data = yaml.load(outfile)
        except yaml.YAMLError as exc:
            print(exc)
        else:
            return data


def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        print('Directory not copied. Error: %s' % e)


def copyfile(src, dest):
    try:
        shutil.copyfile(src, dest)
    except OSError as e:
        print('Directory not copied. Error: %s' % e)


def read_file(file):
    if os.path.isfile(file):
        return True
    else:
        return False


def create_file(file, path, value=None):
    f=open(path+"/"+file, "a+")
    f.write(value)
    f.close()
    try:
        return read_file(path+"/"+file)
    except Exception as e:
        print(e)


def check_folder(path):
    return os.path.isdir(path)


def create_folder(path):
    return os.makedirs(path)


def remove_folder(path):
    return shutil.rmtree(path)


def read_value(file):
    value = open(file)
    return value.read()


# for login deploy
def check_env():
    return os.path.isfile("{}/.prox.env".format(APP_HOME))


def load_env_file():
    return load_dotenv("{}/.prox.env".format(APP_HOME), override=True)

def get_env_values():
    if check_env():
        load_env_file()
        prox_env = {}
        prox_env['username'] = os.environ.get('OS_USERNAME')
        prox_env['password'] = os.environ.get('OS_PASSWORD')
        prox_env['project_url'] = os.environ.get('OS_PROJECT_URL')
        prox_env['project_port'] = os.environ.get('OS_PROJECT_PORT')
        return prox_env
    else:
        print("Can't find prox.env")

def send_http(url, data = None, headers=None):
    send = requests.post(url, json=data, headers=headers)
    respons = send.json()
    return respons

def sign_to_project(url, username, password):
    post_data = {
        "username": username,
        "password": password
    }
    resp = send_http(url, data=post_data)
    return resp


def list_dir(dirname):
    listdir = list()
    for root, dirs, files in os.walk(dirname):
        for file in files:
            data = {
                "index": file,
                "file": os.path.join(root, file)
            }
            listdir.append(data)
    return listdir

def get_http(url, headers=None):
    send = requests.get(url, headers=headers)
    respons = send.json()
    return respons

def make_archive(name, path):
    shutil.make_archive(name,"zip",path)


