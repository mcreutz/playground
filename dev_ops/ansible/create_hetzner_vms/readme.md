ansible-vault encrypt vault.yml

ansible-playbook --ask-vault-pass -i hosts.ini create_hetzner_vms.yml