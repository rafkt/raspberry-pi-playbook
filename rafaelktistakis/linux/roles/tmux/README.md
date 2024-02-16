Tmux
=========

A role that aims to install tmux.
Afer reload, install any new plugins within Tmux by hitting ctl-T and then I
Uninstall removed plugins by ctl-T alt-U
Update plugins by ctl-T U
Note ctl-T is the current defined Tmux prefix for command. Align if you change this. 

Could improve this role by installing the latest through this playbook as:
- wget https://github.com/tmux/tmux/releases/download/3.3a/tmux-3.3a.tar.gz (or latest) or git clone https://github.com/tmux/tmux.git && cd tmux && sh autogen.sh
- sudo apt install libevent-dev
- sudo apt install libncurses-dev

Both of the above are the dependencies required.
Then: 
- ./configure
- make
- sudo make install
- remove the apt tmux package if had been installed
- Add some nice new features like:
    bind -n M-g display-popup -E "tmux new-session -A -s popup"
    you can bind different keys with different popup terminals under different positions with different startup commands

Requirements
------------

N/A

Role Variables
--------------

You can pass ```true``` or ```false``` to the ```install_rpi_scripts``` variable to install or uninstall the rpi scripts. The default is ```true```.


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

