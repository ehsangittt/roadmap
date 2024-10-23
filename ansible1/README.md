## Hello 
##### Here is a doc for you to use ansible. 
##### First of all you have to write playbook.yml.
##### Then you have to run the playbook to know it is work or not.
##### For run the playbook you must have creart inventory.
## Here is a question What is inventory?
##### Inventory is file that you have to write the ip of server that you want to push it on.
For example if you use vm you have to clone your ubuntu and then change the ip.
but also you may use server , in invetory you have to put "username@ip_of_server". but before all you have to do something.
you have to add SSH key to the the destination server. for this job you have to 

```
ssh-copy-id user@ip_address
```
## How to run playbook?
```
 ansible-playbook -i inventory "name of file"
```




