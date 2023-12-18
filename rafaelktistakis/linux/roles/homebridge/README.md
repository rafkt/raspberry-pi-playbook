Home Brdige
=========

Settting up Home bridge role. After installation, complete configuration in http://<ip address of your server>:8581.

Currently supporting plugins for Nest & Wiz accessories.
Configuration turorials can be found under:
- https://practicalhomekit.blogspot.com/2021/09/setting-up-nest-via-homebridge-in.html
- https://github.com/chrisjshull/homebridge-nest#readme
- https://github.com/kpsuperplane/homebridge-wiz-lan


Requirements
------------

N/A

Role Variables
--------------

Variable ```packages``` sets the appropriate packages needs to be installed for a full Home Bridge setup

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
