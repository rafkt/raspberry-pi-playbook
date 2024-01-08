Role Name
=========

This role sets up a cron job to update a Cloudfare DNS record (A type, but also configurable), with the host's IP. The update is done through REST request every 5 minutes.

Requirements
------------

N/A

Role Variables
--------------

The list of variables you can set are:

```domain_name```, ```domain_type```, ```zone_id```, ```record_id```, ```auth_email``` & ```bearer_token```.

Below command is to be used to get current list of DNS records under the zone identifier. Zone identifier obtained through the portal.
 
> curl --request GET \
  --url https://api.cloudflare.com/client/v4/zones/zone_identifier/dns_records \
  --header 'Content-Type: application/json' \
  --header 'X-Auth-Email: '


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
