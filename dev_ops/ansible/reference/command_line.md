# Ansible Command Line Reference

## Basic Commands

### ansible
```bash
ansible <host-pattern> -m <module> -a "<module args>"
```
- `<host-pattern>`: Examples: `all`, `web*`, `myservice.mydomain.com`
- `-m`: Specify module
- `-a`: Module arguments
- `-i`: Specify inventory file
- `-u`: Remote user
- `-b`: Become (sudo)

### ansible-playbook
```bash
ansible-playbook playbook.yml
```
- `-i`: Specify inventory, defaults to `/etc/ansible/hosts`
- `--check`: Dry run
- `--diff`: Show differences
- `-l`: Limit to specific hosts
- `-t`: Only run specific tags, eg. `-t install`, `-t "install,configure"`
- `-v`: Verbose mode (use -vvv for more)

### ansible-vault
```bash
ansible-vault <command> <file>
```
Commands:
- `create`: Create new encrypted file
- `edit`: Edit encrypted file
- `encrypt`: Encrypt existing file
- `decrypt`: Decrypt file
- `view`: View encrypted file
File is a YAML file containing sensitive data.

### ansible-galaxy
```bash
ansible-galaxy install username.role
ansible-galaxy init role_name
```
- `install`: Install role
- `init`: Initialize new role
- `list`: List installed roles
- `search`: Search for roles

## Common Options
- `--version`: Show version
- `--help`: Show help
- `-C`: Check mode (dry run)
- `-K`: Ask for privilege escalation password
- `--list-hosts`: List matched hosts

## Environment Variables
- `ANSIBLE_CONFIG`: Config file path
- `ANSIBLE_INVENTORY`: Inventory file path
- `ANSIBLE_ROLES_PATH`: Role search path