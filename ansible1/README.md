# Hello 
## Here is a doc for you to use ansible. 
### First of all you have to write playbook.yml.
### Then you have to run the playbook to know it is work or not.
## How to run it?
 `ansible-playbook -i inventory "name of file"` 
## Here is a question What is inventory?
### Inventory is file that you have to write the ip of server that you want to push it on.
For example if you use vm you have to clone your ubuntu and then change the ip.
## How to change ip?
### In the settign of ubuntu that you clone you,you have to go to Network, then put it Host-only Adapter insted of Nat.
### Then in terminal write 
 ` "hostname -I " `
