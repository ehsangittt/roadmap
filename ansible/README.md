 ### Here is a doc for you to use ansible.
First of all you have to write playbook.yml.Then you have to run the playbook to know it is work or not.For run the playbook you must have creart inventory.
Here is a question,What is inventory?
Inventory is file that you have to write the ip of server that you want to push it on.For example if you use vm you have to clone your ubuntu and then change the ip.
but also you may use server , in invetory you have to put “username@ip_of_server”. but before all you have to do something.
you have to add SSH key to the the destination server. for this job you have to ssh-copy-id user@ip_address
### How to run playbook?
```ansible-playbook -i inventory name of file ```

For example we have to install docker
There are 2 ways to install docker
`1- online`
For the online version, you don’t need to do anything special. Simply run the playbook, and Docker will be installed for you.
`2-offline`
To install Docker offline, you need to follow a few steps: You need to install the packages in the link below on a system that has internet access,
then place the files in the Playbook, depending on the version you download, and then run the Playbook.
`Note`: You need to go to  this [link](https://download.docker.com),then select the operating system then the version and finally download the files with the .deb extension
`Note`: You need to download the files containerd.io , docker-ce , docker-ce-cli , docker-compose-plugin






