#!/usr/bin/python
# coding: utf8
import subprocess
import sys
import getpass
key_name = "my_key"
try:
    keyid = int(subprocess.Popen("keyctl request user {} @s".format(key_name), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read())
    print(subprocess.Popen("keyctl print {}".format(str(keyid)), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().rstrip())
except ValueError:
    sys.stderr.write("Password for '{}' \n".format(key_name))
    password = getpass.getpass("Vault-pass for vault-id: ").rstrip()
    subprocess.Popen("keyctl add user {} '{}' @s".format(key_name, password), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    keyid = int(subprocess.Popen("keyctl request user {} @s".format(key_name), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read())
    print(subprocess.Popen("keyctl print {}".format(str(keyid)), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().rstrip())
