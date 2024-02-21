Role Name
=========

A role to install flatpak on a linux system.

Requirements
------------

N/A

Role Variables
--------------

Specify whether the installation of gnome or kde backend is desired. No backend is installed by default.
Set the variables `install_gnome_backend` or `install_kde_backend` to `true` to install the desired backend.

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
