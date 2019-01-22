# PROX CLI Orchestration for proxmox

## Setup Env
Setup virtual environment
``` bash
virtualenv -p python3 env
```
Activated Virtualenv
``` bash
source env/bin/activated
```

## Installing
if your development mode
```
pip install -e . 
```

testing mode
```
pip install . 
```

## HELP COMMAND
If you see command list
```
prox -h
```
If you see attribut command
```
prox <command> -h
```

## MIN USAGE
```
prox login
```
Input username, password and host (not in https:// or http://) example:
```
username: username
password: password
host: 10.10.10.10 or host: prox.com
```
default port is 8006 if your setup port (coming soon)

### See Node Cluster
```
prox ls cluster
```
### See VM 
default node : pve
```
prox ls vm
```
if your choose node

```
prox ls vm -N node
```