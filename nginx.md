
# What is nginx?
Nginx is open source software for 
web serving,reverse proxying,caching,load balancing, media streaming and something else like that.for know what is nginx we have to consider nginx is designed as a web server with the best performance.In addition to the http server functionality,nginx can act as proxy server for email service such as EMTP,IMPA,POP3 and a reverse proxy or load balancing system for UDP,TCP AND HTTP servers.
## You might be wondering what a web server is?
In terms of hardware,web server is a stype of server that save web server software and web site componet files such as HTML documents, CSS style sheets and JS files.


## Lets back to nginx.
The goal of nginx is to be fastest web server around. since nginx start to work , another web servers such as apache can not be fast and good like nginx and the html pages become to the dynamic and multifaceted content.Now nginx supports all the components of the modern web inculding web socket, HTTP/2,gRPC and streaming of multiple video formats such as HDS,HLS,RTMP,etc.

# How nginx server works?
Nginx for do the taks,need a little hardware sources and can do the different works in the same time.nginx unlike apache dont make a new process for every HTTP request (..)and this a reason why nginx has a beeter speed and function.(..)
**Nowdays**,many hosting companies use nginx web server because this web server has many **advantages**.
## Lets talk about the advantages
* Nginx has a powerful load balancer
* Has exclusive reverse proxy
* Has cach memory
* Compatibility with different programing such as python and rubi
* Safe and has a good function 
### This are little advantages of the nginx  
---
 **After all** nginx has some disadvantages for example nginx is open source, but users don't have much control over its modules and can't even disable them, so you face limitations for customizing your web server.
### These are brief descripiton of the nginx.

Now you need to install nginx,what should you do?
In step 1 you have to open terminal on ubuntu then you have to type
```
sudo apt update
``` 
and then
 ``` 
 sudo apt install nginx
 ```
*Note : if you have install apache in your sytem before , you cant install nginx, for uninstall apache 
You have to write this order in terminal
``` 
sudo apt-get remove apache
``` 
Then you need to check if Apache is on your system or not for this you have to write this order
``` 
where is apache
``` 


*
Then you after install type "sudo systemctl status nginx" you have to give massage like this "
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Sat 2020-05-02 20:25:43 UTC; 13s ago"
 If you see this , you have install nginx successfully. There is one more way to know is nginx install successfully or no 
 with use  ifconfig in terminal you can find your ip then coppy ip and use it in  http://YOUR_IP . after that if you see welcome to nginx its ok and work.
 
