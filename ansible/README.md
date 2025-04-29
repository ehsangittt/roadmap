## 🐳 Here is a doc for you to use ansible.
`Note:`  If you are in Iran, Docker is blocked for you, and you need to use a VPN or DNS to access it.

First of all you have to add SSH KEY server to `know_hossts`, To do this you have to run this code
```yml
 ssh-keyscan -H "IP_OF_Destination_SERVER" >> ~/.ssh/known_hosts
```
 
Then you should  write playbook.yml.For run the playbook you must have creart inventory.
<br>By looking at inventory.example, you understand inventory.
<br>Before all you have to do something.
you have to add SSH key to the the destination server.
```yml
 ssh-copy-id User@IP_OF_Destination_SERVER
```
### How to run playbook?
```yml
ansible-playbook -i inventory "NAME_OF_FILE"
 ```

We have to install docker
There are 2 ways to install docker

+ Online : 
For the online version, you don’t need to do anything special. Simply run the docker-online.yml , and Docker will be installed for you.

+ Offline :
To install Docker offline, you need to follow a few steps: You need to install the packages in the link below on a system that has internet access,
then place the files in the Playbook, depending on the version you download, and then run the Playbook.

 `Note:`  You need to go to  this [link](https://download.docker.com),then select the operating system then the version and finally download the files with the .deb extension

 `Note:`  You need to download the files containerd.io , docker-ce , docker-ce-cli , docker-compose-plugin

<br>After downloading the files, just like the file I created (vars.yml), copy the version of each file in front of its corresponding file, and then run the playbook.





