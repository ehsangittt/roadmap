#Lets talk about nginx
What is nginx?
Nginx is open source software for web serving,reverse proxying,caching,load balancing, media streaming and something else like that.for know what is nginx we have to consider nginx is designed as a web server with the best performance.In addition to the http server functionality,nginx can act as proxy server for email service such as EMTP,IMPA,POP3 and a reverse proxy or load balancing system for UDP,TCP AND HTTP servers.
You might be wondering what a web server is?
In terms of hardware,web server is a stype of server that save web server software and web site componet files such as HTML documents, CSS style sheets and JS files.
Lets back to nginx.
The goal of nginx is to be fastest web server around. since nginx start to work , another web servers such as apache can not be fast and good like nginx and the html pages become to the dynamic and multifaceted content.Now nginx supports all the components of the modern web inculding web socket, HTTP/2,gRPC and streaming of multiple video formats such as HDS,HLS,RTMP,etc.
How nginx server works?
Nginx for do the taks,need a little hardware sources and can do the different works in the same time.nginx unlike apache dont make a new process for every HTTP request (..)and this a reason why nginx has a beeter speed and function.(..)
Nowdays,many hosting companies use nginx web server because this web server has many advantages.
Lets talk about the advantages
Nginx has a powerful load balancer
Has exclusive reverse proxy
Has cach memory
Compatibility with different programing such as python and rubi
Safe and has a good function 
this are little advantages of the nginx
after all nginx has some disadvantages for example nginx is open source, but users don't have much control over its modules and can't even disable them, so you face limitations for customizing your web server.
These are brief descripiton of the nginx.
Now you need to install nginx,what should you do?
In step 1 you have to open terminal on linux then you have to type "sudo apt update" and then type "sudo apt install nginx"
*Note : if you have install apache in your sytem before , you cant install nginx*
Then you after install type "sudo systemctl status nginx" you have to give massage like this "
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Sat 2020-05-02 20:25:43 UTC; 13s ago"
 If you see this , you have install nginx successfully. There is one more way to know is nginx install successfully or no 
 with use  ifconfig in terminal you can find your ip then coppy ip and use it in  http://YOUR_IP . after that if you see welcome to nginx its ok and work.
 After all you may have some questions like what is load balancer?
 Lets talk about it
 What is a load balancer? A type of technology that distributes the pressure between servers, how do we use it? To improve performance. Reliability and increasing the capacity of the load balancer system as a proxy for web users automatically distributes traffic between servers. There are different types of load balancing, which are: 1- Network traffic load balancing. In this type of network traffic, load balancing is distributed among several servers to improve the performance and efficiency of the system. 2- service layer load balancing In this type of service layer, the user is distributed between several service layers such as database and web service to improve system performance. 3-Hardware load balancing For this type, some hardware devices such as switches and firewalls are used to distribute the workload in the network. It sends a different version of the list of ips, dns requests are evenly distributed among the offending servers to manage the overall routing load. 5- software load balancing software is used to distribute the workload between several servers in this method. In fact, the software can intelligently distribute the load based on various factors such as the current load of the server and the geographical location.
This was one of the types of load balancing, now we have to look at its advantages 1-Increasing reliability: by using load balancer, the workload is regularly distributed between servers, and as a result, the possibility of server failure due to high load is reduced. . 2- Improving performance: By distributing the load between several servers, it is possible to use more processing power and increase performance. So, by using load balancer, the user benefits from better speed and efficiency. 3- Resistance to attacks; The load balancer can act as a defense layer against malicious attacks and thus reduce disruptions. 4- Ease of management: using the load balancer, network administrators can easily add and remove servers. This was load balancing
After this there is one more thing that you want to know and its firewall
A firewall is used to protect our system or network. It can be prepared in software and hardware form. The firewall is placed in the way of the network to communicate with the outside world. In fact, anyone from the outside wants to communicate with our network, and on the contrary, their traffic is controlled by the firewall. In addition to being a firewall for the network, it is also for the operating system, which protects against hacking. Let's go to the ports, the first port is 1024, which of course goes from 0 to 1023, which are called well-known ports. The ports that are used for the main and well-known tasks, for example, port 80 is used for web protocol (http) and port 433 is used for https. Ports below 1023 and below are used for traffic tasks and the use of widely used and famous protocols, and from 1024 and above are unknown ports, and programmers are advised to use these ports so as not to cause interference. In its simplest form, the firewall is managing these ports. Now there are different types of firewalls, the most important of which are 1- packet filtering 2- stateful inspection 3- application filtering 4- next-generation firewall (ngfw) 5- unified threat management (utm) Regarding their definitions, well, in the first step of packet filtering, it says that I can identify up to 4 layers, it recognizes layers 1 to 4, and based on its knowledge of these 4 layers, it can establish security.

