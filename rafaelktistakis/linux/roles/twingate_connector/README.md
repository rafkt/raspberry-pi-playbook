Role Name
=========

A role that spins up a docker container to accomodate twingate connectors. The role supports variable to accomodate seperate connectors under different networks within twingate.
Run ```docker update --restart=no <MY-CONTAINER-ID>``` in case you would like to stop the connector from restarting.
If container fails to start ensure that there is no prior twingate container hanging on the target machine. Run ```docker ps -a``` to review all containers. Run ```docker rm -v `docker ps -a```` to remove all containers (if you really need this).

Requirements
------------

Docker and docker-compose need to be installed in the target system.

Role Variables
--------------
Set the ```connector``` based on the twigate network connectors.
The ```network``` accomodates the twingate networ accomodates the twingate network.
The ```access_token``` and ```refresh_token``` are getting used to authenticate the connector with twingate's network. Those can be also set up in the vault. As such, they have been included in a vault_sample.yml within the root playbook that utilizes this role.

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
