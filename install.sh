#!/bin/sh

# Install ansible packages or update them
# In Debian 12 externall packages e.g. from pip can't be mixed with internal. Use pipx to have this managed or --break-system-packages
sudo apt update && sudo apt install -y python3-dev python3-pip libyaml-dev libffi-dev git pipx && sudo pip3 install --no-binary pyyaml ansible
ansible-galaxy install -r requirements.yml
ansible-galaxy collection install ./rafaelktistakis --force
ansible-playbook main.yml --ask-pass --ask-become-pass
