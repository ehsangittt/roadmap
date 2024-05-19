## What is firewall
In response to what a firewall is, in simple words, it is a layer of security to protect your data on the network and like a bodyguard prevents unauthorized traffic from penetrating your privacy. The firewall determines whether the request is allowed or not by examining each entry. You can request a continuation if requested. If the request is illegal, the firewall blocks the request.
### What is the role of firewall?
Its main task is to carefully inspect all information packets that are going to enter or leave your network. Data packets are like small pieces of a puzzle that are used to transmit information on the Internet.
The firewall only welcomes traffic that has been prearranged to enter.
Examining 7 layers of firewall levels
* Layer 1 (Physical): It is related to the physical transfer of data.
* Layer 2 (Data): It is related to addressing and delivery of data in a local area network.
* Layer 3 (Network): It is related to addressing and data delivery in a wide network.
* Layer 4 (Attack): This layer is related to the management of connections between applications.
* Layer 5 (Session): This layer is related to session management between applications.
* Layer 6 (Display): Related to displaying data to the user.
* Layer 7 (Application): The last layer is related to applications.
### What are the types of firewalls?
 1. Packet-Filtering Firewall; A simple guard
Static packet filtering firewalls are active in the third layer of the network. They check the data packets passing through the network one by one and issue permission to pass based on their origin and destination. Like every time someone wants to enter a parliament, they just check his ID card and if it is valid, let him enter.

Packet filtering firewall
Introducing how the Packet-Filtering Firewall works
 2. session level firewall (Circuit-Level Gateway Firewall); A smart guard
These types of firewalls are active in layer 5. They check the application data packets while communicating and if they are healthy, they establish a stable connection between the two networks. After the connection is established, the firewall no longer monitors it.

Compared to the previous type, this firewall goes one step further and pays attention not only to the address, but also to the type of communication between the sender and receiver. In addition to the origin and destination, he also checks the communication status and the safe path for information exchange. The session-level firewall has nothing to do with packet content. It means that if someone abuses this safe path, he can't do anything.

 3. Stateful Inspection Firewall; All-round guard
What is meant by this type of firewall? Unlike static packet filter firewalls, this firewall has the ability to monitor current communications and remember past communications. They started at layer 4 and today can monitor multiple layers, including the application layer (layer 7).

This all-in-one watchdog checks what packets have already been exchanged and based on that it decides whether to allow a new packet to enter or not. In other words, it takes into account the history of communication. Just like the guard, in addition to the ID card, knows each person by his face and history.

How the level inspection firewall works
Stateful Inspection Firewall work process
 4. Proxy Firewall (Proxy Firewall); Strict security specialist
Proxy firewalls are another type of firewall known as programming level (layer 7) firewalls. This type of firewall is unique in reading and filtering programming protocols. Proxy firewalls are a combination of programmatic level inspection, "deep packet inspection (DPI)", or dynamic packet inspection.

This guard has the status of a security expert. In addition to checking packages, it also reads their contents. That is, it detects, for example, what an e-mail contains, and based on that, it decides whether to reach the destination or not. Just like a strict guard, this firewall checks every packet of information to make it easy to worry about security. Of course, this high accuracy lowers the network speed.

How the proxy firewall works
Check packages and their contents with proxy firewall
 5. Next-Generation Firewall; Advanced guard
Evolving threats require better solutions, and next-generation firewalls are at the forefront of firewalls by combining the features of a traditional firewall with network intrusion prevention systems (IPS).

This firewall is a combination of all previous firewalls. In fact, in addition to being a filter, it checks the status of communications and the contents of packets. It can also automatically detect new threats and block them.

 6. Hybrid firewall; Combined guard
What is meant by this firewall? As the name suggests, hybrid firewalls use two or more types of firewalls in a single private network. That is, it combines the advantages of different types of firewalls and creates a more comprehensive security solution.
For example, a hybrid firewall might use a dynamic packet inspection firewall to filter public traffic and a proxy firewall to filter sensitive traffic.
What is a software firewall? From essential computer programs to servers
A software firewall is a computer program that is installed on a computer or server and is responsible for protecting the network from unwanted traffic.
What is a hardware firewall? Computer independent system
A hardware firewall is an independent system that operates separately from the computer and filters incoming information from the Internet. If you have an Internet modem router, it probably has a hardware firewall.
### What is the use of firewall?
1. Defense against threats
 2. Recording and reviewing activities 
 3. Traffic filtering 
  4. Access control and blocking
### What are the advantages and disadvantages of firewall?
**4 examples of firewall advantages**
1. Privacy shield and network security
2. Light speed against attacks
3. Security rules
4. Protection against deception and fraud
#### Lets look at the disavantages
1. Constant attention on heavy traffic
2. The double-edged sword of firewall rules
3. Limited vision, limited power
