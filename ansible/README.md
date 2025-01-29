<p class="has-line-data" data-line-start="0" data-line-end="1">GNU nano 7.2                                                                   <a href="http://README.md">README.md</a></p>
<h2 class="code-line" data-line-start=1 data-line-end=2 ><a id="Hello_1"></a>Hello</h2>
<p class="has-line-data" data-line-start="2" data-line-end="8">Here is a doc for you to use ansible.<br>
First of all you have to write playbook.yml.Then you have to run the playbook to know it is work or not.For run the playbook you must have creart inventory.<br>
Here is a question What is inventory?<br>
Inventory is file that you have to write the ip of server that you want to push it on.For example if you use vm you have to clone your ubuntu and then change the ip.<br>
but also you may use server , in invetory you have to put “username@ip_of_server”. but before all you have to do something.<br>
you have to add SSH key to the the destination server. for this job you have to</p>
<pre><code class="has-line-data" data-line-start="10" data-line-end="12">ssh-copy-id user@ip_address
</code></pre>
<h2 class="code-line" data-line-start=12 data-line-end=13 ><a id="How_to_run_playbook_12"></a>How to run playbook?</h2>
<pre><code class="has-line-data" data-line-start="14" data-line-end="16"> ansible-playbook -i inventory &quot;name of file&quot;
</code></pre>
<hr>
<p class="has-line-data" data-line-start="18" data-line-end="28">For example we have to install docker<br>
There are 2 ways to install docker<br>
1- online<br>
For the online version, you don’t need to do anything special. Simply run the playbook, and Docker will be installed for you.<br>
2-offline<br>
To install Docker offline, you need to follow a few steps: You need to install the packages in the link below on a system that has internet access,<br>
then place the files in the Playbook, depending on the version you download, and then run the Playbook.<br>
Note: You need to go to this <a href="https://download.docker.com/">link</a><br>
then select the operating system then the version and finally download the files with the .deb extension<br>
Note: You need to download the files <a>containerd.io</a> , docker-ce , docker-ce-cli , docker-compose-plugin</p>
