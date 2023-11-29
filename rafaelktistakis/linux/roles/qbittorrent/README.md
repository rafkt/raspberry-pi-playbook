QBitTorrent
=========

Installs qbittorrent.

Requirements
------------

N/A

Role Variables
--------------

You can override the default packages installed through the ```packages``` variable of this role
Set variable ```service_started``` in order to define whether the service should be on start state after the role installation and on each reboot

Dependencies
------------

N/A

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
