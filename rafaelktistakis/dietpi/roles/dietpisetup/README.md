Role Name
=========

Initial setup of dietpi

Requirements
------------

OpenSsh & a valid user with pass defined in the vault.

Role Variables
--------------
For setting the headless behaviour, set the ```enable_headless``` to 1 or 0 respectively.
The swap size is set through the ```swap_size``` in MB.
To have the boot behaviour on having console to autostart (without user interface), set the ```console_autostart``` to 0. Alternatively, set it to 7 for console autologin behaviour. The ```console_autologin``` holds the value 7 in the defaults, so one could set the ```console_autologin``` into ```console_autostart```.


Dependencies
------------

This role is tightly coupled with the dietpi-config untilities offerred under a dietpi distribution. The aim is to automate such configuration to dietpi which can enable a headless setup. 

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
