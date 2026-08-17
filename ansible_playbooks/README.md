# Ansible

## Testing system

Instructions on how to set up a testing system for ansible are found in the Docker/ directory.

In `inventory/group_vars/myhosts` lies a template for the vault (`vault.template.yml`). Fill it with the username and the password for the remote machine and save it as `vault.yml`. Don't ever commit it. The directory in which the vault lies has to match to definition in the `inventory/inventory.yml`. Changing one without changing the other leads to the vault not beeing detected.

Test the connection with either
```bash
ansible myhosts -m ping -i inventory.ini
```
or
```bash
ansible docky -m ping -i inventory.yml
```
depending on whether you want to go with .ini or .yml.