#!/bin/sh

# Install ansible packages or update them
# In Debian 12 externall packages e.g. from pip can't be mixed with internal. Use pipx to have this managed or --break-system-packages
sudo apt update && sudo apt install -y python3-dev python3-pip libyaml-dev libffi-dev git pipx && sudo pip3 install --no-binary pyyaml ansible
ansible-galaxy install -r requirements.yml
ansible-galaxy collection install ./rafaelktistakis --force
ansible-playbook main.yml

# For flexibility although bad practise, you can disable sudo password for target user.
# sudo visudo /etc/sudoers.d/010_pi-nopasswd
# If in bullseye
# or 
# sudo visudo
# if newer debian
# Add user ALL=(ALL) NOPASSWD: ALL
# or revert to user ALL=(ALL) ALL
# Alternatively use ansible-vault to encrypt the password and use it in the playbook:
# ansible-vault create vault.yml
# ansible-vault encrypt vault.yml --vault-id my_key@./scripts/run_key.sh --encrypt-vault-id my_key
# ansible-vault decrypt vault.yml --vault-id my_key@./scripts/run_key.sh
# Above encrypt/dectypt uses keyctl as the backend key manager.
# Usefule keyctl commands:
# keyctl request user my_key, keyctl print <key-id>, keyctl revoke <key-id>