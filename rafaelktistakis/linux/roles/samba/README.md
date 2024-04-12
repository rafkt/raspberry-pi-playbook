Role Name
=========

A role to install Samba server on the system.
Some parameters i.e. for user setup and file shares are supported.

Add user to the server by running ```smbpasswd -a rafaelktistakis```

More configuration ideas, e.g. for Apple Time Capsule Share, can be found udner Files of the role.

Requirements
------------

N/A

Role Variables
--------------

Set the ```smb_conf``` as a multiline, block-in-file segment to be added at the end of the smb.conf.
Original/previous smb.conf is getting backedup to avoid misconfiguration if you somehow clobbered it incorrectly.
Some global configuration is set under the ```global_smb_conf``` variable. Default values have been assigned based on some host configuration.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

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
