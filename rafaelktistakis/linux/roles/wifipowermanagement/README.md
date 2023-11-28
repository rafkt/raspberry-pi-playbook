wifipowermanagement
=========

A simple role to turn on/off the wlan0 power management through /etc/rc.local

Requirements
------------

N/A

Role Variables
--------------

Set the variable ```power``` to off / on for off/on the wlan0 power management
Set variable ```active``` to 0 / 1 for executing a system reboot if gateway is not reachable for a period of time
Set variable ```gateway``` to set the gateway which shall be pinged if monitorreboot is enabled

Dependencies
------------

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
