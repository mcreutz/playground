# Ansible Command Cheat Sheet

## Basic Commands
### Ad-hoc Commands
```bash
# Check connectivity to remote host
ansible remote.example.com -m ping

# Get system information from server
ansible remote.example.com -m setup

# Execute command on server
ansible 10.0.0.1 -m command -a "df -h"

# Run commands with sudo on remote server
ansible remote.example.com -m command -a "whoami" --become
```

### System Commands
```bash
# Display ansible version
ansible --version

# Show configuration
ansible-config dump

# List available modules
ansible-doc -l

# Get help for specific module
ansible-doc ping
```

### Common Options
- `-v`: Verbose mode
- `-vvv`: More verbose
- `--tags`: Run specific tags
- `--skip-tags`: Skip specific tags
- `-l`: Limit to specific hosts
- `-e`: Set extra variables
- `--become`: Execute tasks with privilege escalation (sudo)
- `--become-ask-pass`: Prompt for privilege escalation password


## Configuration
Ansible uses configuration files to define its behavior and settings.
- `/etc/ansible/ansible.cfg`: Global system-wide configuration
- `./ansible.cfg`: Project-specific configuration (takes precedence)

Example configuration:
```ini
# ansible.cfg
[defaults]
inventory = ./inventory.yml
remote_user = ansible
private_key_file = ~/.ssh/id_rsa
host_key_checking = False

[privilege_escalation]
become = True
become_method = sudo
become_user = root
```


## Inventory Management
Inventory files define the hosts and groups that Ansible manages. They can be in INI or YAML format.
- Default: `/etc/ansible/hosts`
- Custom: Specified in ansible.cfg or via `-i` option

```yaml
# inventory.yml
all:
  hosts:
    web1.example.com:
    web2.example.com:
    db1.example.com:
  children:
    webservers:
      hosts:
        web1.example.com:
        web2.example.com:
    dbservers:
      hosts:
        db1.example.com:
```

Inventory Usage:
```bash
# List all hosts
ansible all --list-hosts

# Check connectivity to all hosts
ansible -i inventory.ini --ping

# Execute uptime command on all hosts
ansible all -a "uptime"

# Execute uptime command on specific group
ansible webservers -a "uptime"

# Execute uptime command on specific host
ansible web1.example.com -a "uptime"
```


## Modules
Modules are reusable units of code that Ansible executes on managed hosts. They are the building blocks for tasks.

Common modules:
- `apt/yum`: Package management
- `copy`: Copy files
- `file`: File operations
- `service`: Manage services
- `template`: Template processing

Using modules:
```yaml
# File operations
- name: Create directory
  file:
    path: /app/data
    state: directory
    mode: '0755'

# Service management
- name: Start service
  service:
    name: nginx
    state: started
    enabled: yes
```


## Playbooks
Playbooks are YAML files that define automation tasks in Ansible. They contain a list of plays, each defining a set of tasks to execute on specific hosts.

Example playbook:
```yaml
# example-playbook.yml
- hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

Running playbooks:
```bash
# Run playbook
ansible-playbook playbook.yml

# Run playbook with inventory file
ansible-playbook -i inventory.yml playbook.yml

# Check syntax
ansible-playbook --syntax-check playbook.yml

# Dry run (simulation)
ansible-playbook --check playbook.yml
```


## Best Practices
- Always use YAML format
- Version control your playbooks
- Use roles for reusable content
- Test with `--check` before running