# Ansible

## Testing system

Instructions on how to set up a testing system for ansible are found in the Docker/ directory.

Test the connection with either
```bash
ansible myhosts -m ping -i inventory.ini
```
or
```bash
ansible docky -m ping -i inventory.yml
```
depending on whether you want to go with .ini or .yml.